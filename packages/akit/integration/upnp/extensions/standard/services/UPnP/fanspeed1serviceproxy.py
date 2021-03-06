"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class FanSpeed1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'FanSpeed1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:FanSpeed:1'

    SERVICE_EVENT_VARIABLES = {}

    def action_GetFanDirection(self, extract_returns=True):
        """
            Calls the GetFanDirection action.

            :returns: "CurrentDirectionStatus"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFanDirection", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentDirectionStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetFanDirectionTarget(self, extract_returns=True):
        """
            Calls the GetFanDirectionTarget action.

            :returns: "CurrentDirectionTarget"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFanDirectionTarget", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentDirectionTarget",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetFanSpeed(self, extract_returns=True):
        """
            Calls the GetFanSpeed action.

            :returns: "CurrentFanSpeedStatus"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFanSpeed", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentFanSpeedStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetFanSpeedTarget(self, extract_returns=True):
        """
            Calls the GetFanSpeedTarget action.

            :returns: "CurrentFanSpeedTarget"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFanSpeedTarget", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentFanSpeedTarget",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetFanDirection(self, NewDirectionTarget, extract_returns=True):
        """
            Calls the SetFanDirection action.

            :returns: "result"
        """
        arguments = {
            "NewDirectionTarget": NewDirectionTarget,
        }

        out_params = self._proxy_call_action("SetFanDirection", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetFanSpeed(self, NewFanSpeedTarget, extract_returns=True):
        """
            Calls the SetFanSpeed action.

            :returns: "result"
        """
        arguments = {
            "NewFanSpeedTarget": NewFanSpeedTarget,
        }

        out_params = self._proxy_call_action("SetFanSpeed", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
