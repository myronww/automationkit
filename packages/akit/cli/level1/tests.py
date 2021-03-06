
__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import argparse
import os
import sys

import click

from akit.environment.variables import LOG_LEVEL_NAMES

@click.group("tests")
def group_tests():
    return

HELP_ROOT = "The root directory to use when scanning for tests."
HELP_EXCLUDES = "Add a test inclusion expression."
HELP_INCLUDES = "Add a test exclusion expression."
HELP_OUTPUT = "The output directory where results and artifacts are collected."
HELP_START = r"A time stamp to associate with the start of the run. Example: 2020-10-17T15:30:11.989120  Bash: date +%Y-%m-%dT%H:%M:%S.%N"
HELP_BRANCH = "The name of the branch to associate with the test run results."
HELP_BUILD = "The name of the build to associate with the test run results."
HELP_FLAVOR = "The name of the flavor to associate with the test run results."
HELP_CONSOLE_LOG_LEVEL = "The logging level for console output."
HELP_FILE_LOG_LEVEL = "The logging level for logfile output."
HELP_DEBUG = "Output debug information to the console."

@click.command("query")
@click.option("--root", default=".", type=str, help=HELP_ROOT)
@click.option("--excludes", "-x", multiple=True, help=HELP_EXCLUDES)
@click.option("--includes", "-i", multiple=True, help=HELP_INCLUDES)
@click.option("--debug", default=False, type=bool, help=HELP_DEBUG)
def command_tests_query(root, includes, excludes, debug):
    # pylint: disable=unused-import,import-outside-toplevel

    # We do the imports of the automation framework code inside the action functions because
    # we don't want to startup loggin and the processing of inputs and environment variables
    # until we have entered an action method.  Thats way we know how to setup the environment.

    # IMPORTANT: We need to load the context first because it will trigger the loading
    # of the default user configuration
    from akit.environment.context import Context
    from akit.environment.variables import extend_path

    ctx = Context()
    env = ctx.lookup("/environment")

    # Set the jobtype
    env["jobtype"] = "testrun"

    test_root = os.path.abspath(os.path.expandvars(os.path.expanduser(root)))
    if not os.path.isdir(test_root):
        errmsg = "The specified root folder does not exist. root=%s" % root
        if test_root != root:
            errmsg += " expanded=%s" % test_root
        raise click.BadParameter(errmsg)

    # Make sure we extend PATH to include the test root
    extend_path(test_root)

    # We use console activation because all our input output is going through the terminal
    import akit.environment.console

    from akit.testing.unittest.testcollector import TestCollector

    collector = TestCollector(root, excludes, method_prefix="test")

    # Discover the tests, integration points, and scopes.  If test modules is not None then
    # we are running tests from an individual module and we can limit discovery to the test module
    for inc_item in includes:
        collector.collect_references(inc_item)

    collector.collect_testpacks()

    collector.expand_testpacks()

    for tpname, tpobj in collector.test_packages.items():
        print()
        print("TestPack - %s" % tpname)

        testnames = [k for k in tpobj.test_references.keys()]
        testnames.sort()
        for tname in testnames:
            print("    " + tname)

    print()

    print("IMPORT ERRORS:", file=sys.stderr)
    for ifilename, _ in collector.import_errors.items():
        imperr_msg = ifilename
        print("    " + imperr_msg, file=sys.stderr)
    print("", file=sys.stderr)

    return

@click.command("run")
@click.option("--root", default=".",  type=str, required=False, help=HELP_ROOT)
@click.option("--excludes", "-x", multiple=True, required=False, help=HELP_EXCLUDES)
@click.option("--includes", "-i", multiple=True, help=HELP_INCLUDES)
@click.option("--output", "-o", required=False, help=HELP_OUTPUT)
@click.option("--start", default=None, required=False, help=HELP_START)
@click.option("--branch", default=None, required=False, help=HELP_BRANCH)
@click.option("--build", default=None, required=False, help=HELP_BUILD)
@click.option("--flavor", default=None, required=False, help=HELP_FLAVOR)
@click.option("--console-level", default=None, required=False, type=click.Choice(LOG_LEVEL_NAMES, case_sensitive=False), help=HELP_CONSOLE_LOG_LEVEL)
@click.option("--logfile-level", default=None, required=False, type=click.Choice(LOG_LEVEL_NAMES, case_sensitive=False), help=HELP_FILE_LOG_LEVEL)
def command_tests_run(root, includes, excludes, output, start, branch, build, flavor, console_level, logfile_level):

    # pylint: disable=unused-import,import-outside-toplevel

    # We do the imports of the automation framework code inside the action functions because
    # we don't want to startup loggin and the processing of inputs and environment variables
    # until we have entered an action method.  Thats way we know how to setup the environment.

    # IMPORTANT: We need to load the context first because it will trigger the loading
    # of the default user configuration
    from akit.environment.context import Context

    from akit.compat import import_by_name
    from akit.environment.variables import extend_path, JOB_TYPES

    try:
        ctx = Context()
        env = ctx.lookup("/environment")

        # Set the jobtype
        env["jobtype"] = JOB_TYPES.TESTRUN

        test_root = os.path.abspath(os.path.expandvars(os.path.expanduser(root)))
        if not os.path.isdir(test_root):
            errmsg = "The specified root folder does not exist. root=%s" % root
            if test_root != root:
                errmsg += " expanded=%s" % test_root
            raise click.BadParameter(errmsg)

        # Make sure we extend PATH to include the test root
        extend_path(test_root)

        # We perform activation a little later in the testrunner.py file so we can
        # handle exceptions in the context of testrunner_main function
        import akit.environment.activate
        from akit.xlogging.foundations import logging_initialize, getAutomatonKitLogger

        # Initialize logging
        logging_initialize()
        logger = getAutomatonKitLogger()

        from akit.testing.unittest.testjob import DefaultTestJob

        # At this point in the code, we either lookup an existing test job or we create a test job
        # from the includes, excludes or test_module
        TestJobType = DefaultTestJob

        result_code = 0
        with TestJobType(logger, test_root, includes=includes, excludes=excludes) as tjob:
            result_code = tjob.execute()

        sys.exit(result_code)

    finally:
        pass

    return

group_tests.add_command(command_tests_query)
group_tests.add_command(command_tests_run)
