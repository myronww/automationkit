
"""
.. module:: results
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains the :class:`TaskBase` object which is used as the base.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import collections
import enum
import json
import os
import time

from akit.xtime import format_time_with_fractional

class ResultCode(enum.IntEnum):
    """
        Enumeration that summarizes a result.
    """
    UNSET = 0
    PASSED = 1
    SKIPPED = 2
    ERRORED = 3
    FAILED = 4
    UNKOWN = 5

class ResultType(enum.IntEnum):
    """
        Enumeration that identifies the type of result object.
    """
    JOB = 0
    PACKAGE = 1
    SCOPE = 2
    TASK_CONTAINER = 3
    TASK = 4
    TEST_CONTAINER = 5
    TEST = 6
    STEP_CONATINER = 7
    STEP = 8

class ResultNode:
    """
        The :class:`ResultNode` object represents the information associated with a node in a tree of results.
        The :class:`ResultNode` object stores information about a node that has detailed results information
        associated with a task, test or step.
    """
    def __init__(self, result_inst, result_name, result_type, result_code=ResultCode.UNSET, parent_inst=None):
        """
            Initializes an instance of a :class:`ResultNode` object that represent the information associated with
            a specific result in a result tree.

            :param result_inst: The unique identifier to link this result container with its children.
            :type result_inst: str
            :param result_name: The name of the result container.
            :type result_name: str
            :param result_type: The type :class:`ResultType` type code of result container.
            :type result_inst: :class:`ResultType`
            :param result_code:
            :type result_code: :class:`ResultCode`
            :param parent_inst: The unique identifier fo this result nodes parent.
            :type parent_inst: str
        """
        self._result_inst = result_inst
        self._result_name = result_name
        self._parent_inst = parent_inst
        self._result_code = result_code
        self._result_type = result_type
        self._start = time.time()
        self._stop = None
        self._errors = []
        self._failures = []
        self._warnings = []
        self._reason = None
        self._docstr = None
        return

    @property
    def parent_inst(self):
        """
            The unique identifier fo this result nodes parent.
        """
        return self._parent_inst

    @property
    def result_code(self):
        """
            The type :class:`ResultType` type code of result container.
        """
        return self._result_code

    @property
    def result_inst(self):
        """
            The unique identifier to link this result container with its children.
        """
        return self._result_inst

    @property
    def result_name(self):
        """
            The name of the result item.
        """
        return self._result_name

    @property
    def result_type(self):
        """
            The :class:`ResultType` code associated with this result node.
        """
        return self._result_type

    def add_error(self, err_lines):
        """
            Adds error trace lines for a single error to this result node.
        """
        trim_lines = []
        for nline in err_lines:
            nline = nline.rstrip()
            nlindex = nline.find(os.linesep)
            if nlindex > -1:
                trim_lines.append(nline[:nlindex])
                trim_lines.append(nline[nlindex + 1:])
            else:
                trim_lines.append(nline)
        self._errors.append(trim_lines)
        return

    def add_failure(self, fail_lines):
        """
            Adds failure trace lines for a single failure to this result node.
        """
        trim_lines = []
        for nline in fail_lines:
            nline = nline.rstrip()
            nlindex = nline.find(os.linesep)
            if nlindex > -1:
                trim_lines.append(nline[:nlindex])
                trim_lines.append(nline[nlindex + 1:])
            else:
                trim_lines.append(nline)
        self._failures.append(trim_lines)
        return

    def add_warning(self, warn_lines):
        """
            Adds warning trace lines for a single warning to this result node.
        """
        trim_lines = []
        for nline in warn_lines:
            nline = nline.rstrip()
            nlindex = nline.find(os.linesep)
            if nlindex > -1:
                trim_lines.append(nline[:nlindex])
                trim_lines.append(nline[nlindex + 1:])
            else:
                trim_lines.append(nline)
        self._warnings.append(trim_lines)
        return

    def set_documentation(self, docstr):
        """
            Sets the documentation string associated with this result node.
        """
        self._docstr = docstr
        return

    def finalize(self):
        """
            Finalizes the :class:`ResultCode` code for this result node based on whether
            there were any errors or failures added to the node.
        """
        self._stop = time.time()

        if len(self._failures) > 0:
            self._result_code = ResultCode.FAILED
        elif len(self._errors) > 0:
            self._result_code = ResultCode.ERRORED
        elif self._result_code == ResultCode.UNSET:
            self._result_code = ResultCode.UNKOWN

        return

    def mark_passed(self):
        """
            Marks this result with a :class:`ResultCode` of ResultCode.PASSED
        """
        self._result_code = ResultCode.PASSED
        return

    def mark_skip(self, reason):
        """
            Marks this result with a :class:`ResultCode` of ResultCode.SKIPPED

            :param reason: The reason the task or test this result is associated with was skipped.
            :type reason: str
        """
        self._reason = reason
        self._result_code = ResultCode.SKIPPED
        return

    def to_json(self):
        """
            Convers the result node instance to JSON format
        """

        detail = collections.OrderedDict([
            ("reason", self._reason),
            ("errors", self._errors),
            ("failures", self._failures),
            ("warnings", self._warnings)
        ])

        if self._docstr is not None:
            detail["documentation"] =  self._docstr

        start_datetime = format_time_with_fractional(self._start)
        stop_datetime = format_time_with_fractional(self._stop)

        jobj = collections.OrderedDict([
            ("name", self._result_name),
            ("instance", self._result_inst),
            ("parent", self._parent_inst),
            ("rtype", self._result_type.name),
            ("result", self._result_code.name),
            ("start", start_datetime),
            ("stop", stop_datetime),
            ("detail", detail)
        ])

        jstr = json.dumps(jobj, indent=4)

        return jstr

class ResultContainer:
    """
        The :class:`ResultContainer` is a object that contains the information that represents the
        relationship between a result container and the result nodes in a result tree.
    """
    def __init__(self, result_inst, result_name, result_type, parent_inst=None):
        """
            Creates an instance of a result container.

            :param result_inst: The unique identifier to link this result container with its children.
            :type result_inst: str
            :param result_name: The name of the result container.
            :type result_name: str
            :param result_type: The type :class:`ResultType` type code of result container.
            :type result_inst: :class:`ResultType`
            :param parent_inst: The unique identifier fo this result nodes parent.
            :type parent_inst: str
        """
        self._result_inst = result_inst
        self._result_name = result_name
        self._parent_inst = parent_inst
        self._result_type = result_type
        return

    @property
    def parent_inst(self):
        """
            The unique identifier fo this result nodes parent.
        """
        return self._parent_inst

    @property
    def result_inst(self):
        """
            The unique identifier to link this result container with its children.
        """
        return self._result_inst

    @property
    def result_name(self):
        """
            The name of the result container.
        """
        return self._result_name

    @property
    def result_type(self):
        """
            The type :class:`ResultType` type code of result container.
        """
        return self._result_type

    def to_json(self):
        """
            Convers the result container instance to JSON format
        """
        jobj = collections.OrderedDict([
            ("name", self._result_name),
            ("instance", self._result_inst),
            ("parent", self._parent_inst),
            ("rtype", self._result_type.name)
        ])

        jstr = json.dumps(jobj, indent=4)

        return jstr
