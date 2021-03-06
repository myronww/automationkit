"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class InputConfig1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'InputConfig1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:InputConfig:1'

    SERVICE_EVENT_VARIABLES = {
        "DeviceInputCapability": { "data_type": "string", "default": None, "allowed_list": None},
        "RequiredInputType": { "data_type": "string", "default": None, "allowed_list": None},
    }

    def action_GetInputCapability(self, extract_returns=True):
        """
            Calls the GetInputCapability action.

            :returns: "SupportedCapabilities"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetInputCapability", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SupportedCapabilities",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetInputConnectionList(self, extract_returns=True):
        """
            Calls the GetInputConnectionList action.

            :returns: "CurrentConnectionList"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetInputConnectionList", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentConnectionList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetInputSession(self, SelectedCapability, ReceiverInfo, PeerDeviceInfo, extract_returns=True):
        """
            Calls the SetInputSession action.

            :returns: "SessionID", "ConnectionInfo"
        """
        arguments = {
            "SelectedCapability": SelectedCapability,
            "ReceiverInfo": ReceiverInfo,
            "PeerDeviceInfo": PeerDeviceInfo,
        }

        out_params = self._proxy_call_action("SetInputSession", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SessionID", "ConnectionInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetMonopolizedSender(self, OwnerDeviceInfo, OwnedSessionID, extract_returns=True):
        """
            Calls the SetMonopolizedSender action.

            :returns: "result"
        """
        arguments = {
            "OwnerDeviceInfo": OwnerDeviceInfo,
            "OwnedSessionID": OwnedSessionID,
        }

        out_params = self._proxy_call_action("SetMonopolizedSender", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetMultiInputMode(self, NewMultiInputMode, extract_returns=True):
        """
            Calls the SetMultiInputMode action.

            :returns: "result"
        """
        arguments = {
            "NewMultiInputMode": NewMultiInputMode,
        }

        out_params = self._proxy_call_action("SetMultiInputMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StartInputSession(self, SessionID, extract_returns=True):
        """
            Calls the StartInputSession action.

            :returns: "result"
        """
        arguments = {
            "SessionID": SessionID,
        }

        out_params = self._proxy_call_action("StartInputSession", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StopInputsession(self, SessionID, extract_returns=True):
        """
            Calls the StopInputsession action.

            :returns: "result"
        """
        arguments = {
            "SessionID": SessionID,
        }

        out_params = self._proxy_call_action("StopInputsession", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SwitchInputSession(self, SessionID, extract_returns=True):
        """
            Calls the SwitchInputSession action.

            :returns: "result"
        """
        arguments = {
            "SessionID": SessionID,
        }

        out_params = self._proxy_call_action("SwitchInputSession", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
