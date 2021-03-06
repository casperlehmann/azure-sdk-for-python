# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PowerShellCommandResult(Model):
    """Results from invoking a PowerShell command.

    :param message_type: The type of message.
    :type message_type: int
    :param foreground_color: The HTML color string representing the foreground
     color.
    :type foreground_color: str
    :param background_color: The HTML color string representing the background
     color.
    :type background_color: str
    :param value: Actual result text from the PowerShell Command.
    :type value: str
    :param prompt: The interactive prompt message.
    :type prompt: str
    :param exit_code: The exit code from a executable that was called from
     PowerShell.
    :type exit_code: int
    :param id: ID of the prompt message.
    :type id: int
    :param caption: Text that precedes the prompt.
    :type caption: str
    :param message: Text of the prompt.
    :type message: str
    :param descriptions: Collection of PromptFieldDescription objects that
     contains the user input.
    :type descriptions:
     list[~azure.mgmt.servermanager.models.PromptFieldDescription]
    """

    _attribute_map = {
        'message_type': {'key': 'messageType', 'type': 'int'},
        'foreground_color': {'key': 'foregroundColor', 'type': 'str'},
        'background_color': {'key': 'backgroundColor', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'prompt': {'key': 'prompt', 'type': 'str'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'id': {'key': 'id', 'type': 'int'},
        'caption': {'key': 'caption', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'descriptions': {'key': 'descriptions', 'type': '[PromptFieldDescription]'},
    }

    def __init__(self, **kwargs):
        super(PowerShellCommandResult, self).__init__(**kwargs)
        self.message_type = kwargs.get('message_type', None)
        self.foreground_color = kwargs.get('foreground_color', None)
        self.background_color = kwargs.get('background_color', None)
        self.value = kwargs.get('value', None)
        self.prompt = kwargs.get('prompt', None)
        self.exit_code = kwargs.get('exit_code', None)
        self.id = kwargs.get('id', None)
        self.caption = kwargs.get('caption', None)
        self.message = kwargs.get('message', None)
        self.descriptions = kwargs.get('descriptions', None)
