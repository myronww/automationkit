"""
.. module:: windowsclientmixin
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains a WindowsClientMixIn object to use for working with Windows clients

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

from akit.mixins.integration import IntegrationMixIn

class WindowsClientMixIn(IntegrationMixIn):
    """
        This is a mock playback device.
    """

    pathbase = "clients/windows"

    def __init__(self, *args, **kwargs):
        """
            The default contructor for an :class:`WindowsClientMixIn`.
        """
        super(WindowsClientMixIn, self).__init__(*args, role=role, **kwargs)

        if self.pathbase is None:
            raise ValueError("The 'pathbase' class member variable must be set to a unique name for each integration class type.")

        self.context.insert(self.pathbase, self)
        return

    @classmethod
    def attach_to_environment(cls, landscape):
        """
            This API is called so that the IntegrationMixIn can process configuration information.  The :class:`IntegrationMixIn`
            will verify that it has a valid environment and configuration to run in.

            :raises :class:`akit.exceptions.AKitMissingConfigError`, :class:`akit.exceptions.AKitInvalidConfigError`:
        """

        return

    @classmethod
    def collect_resources(cls):
        """
            This API is called so the `IntegrationMixIn` can connect with a resource management
            system and gain access to the resources required for the automation run.

            :raises :class:`akit.exceptions.AKitResourceError`:
        """

        return

    @classmethod
    def diagnostic(cls, diag_level, diag_folder):
        """
            The API is called by the :class:`akit.sequencer.Sequencer` object when the automation sequencer is
            building out a diagnostic package at a diagnostic point in the automation sequence.  Example diagnostic
            points are:

            * pre-run
            * post-run

            Each diagnostic package has its own storage location so derived :class:`akit.scope.ScopeMixIn` objects
            can simply write to their specified output folder.

            :param diag_level: The maximum diagnostic level to run dianostics for.
            :type diag_level: int
            :param diag_folder: The output folder path where the diagnostic information should be written.
            :type diag_folder: str
        """

        return

    @classmethod
    def establish_connectivity(cls):
        """
            This API is called so the `IntegrationMixIn` can establish connectivity with any compute or storage
            resources.

            :raises :class:`akit.exceptins.AKitInitialConnectivityError`:
        """

        return
