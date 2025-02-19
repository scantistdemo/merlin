# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from client.configuration import Configuration


class Transformer(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'transformer_type': 'str',
        'image': 'str',
        'command': 'str',
        'args': 'str',
        'resource_request': 'ResourceRequest',
        'env_vars': 'list[EnvVar]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'enabled': 'enabled',
        'transformer_type': 'transformer_type',
        'image': 'image',
        'command': 'command',
        'args': 'args',
        'resource_request': 'resource_request',
        'env_vars': 'env_vars',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, enabled=None, transformer_type=None, image=None, command=None, args=None, resource_request=None, env_vars=None, created_at=None, updated_at=None, _configuration=None):  # noqa: E501
        """Transformer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._transformer_type = None
        self._image = None
        self._command = None
        self._args = None
        self._resource_request = None
        self._env_vars = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if transformer_type is not None:
            self.transformer_type = transformer_type
        if image is not None:
            self.image = image
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if resource_request is not None:
            self.resource_request = resource_request
        if env_vars is not None:
            self.env_vars = env_vars
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def enabled(self):
        """Gets the enabled of this Transformer.  # noqa: E501


        :return: The enabled of this Transformer.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Transformer.


        :param enabled: The enabled of this Transformer.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def transformer_type(self):
        """Gets the transformer_type of this Transformer.  # noqa: E501


        :return: The transformer_type of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._transformer_type

    @transformer_type.setter
    def transformer_type(self, transformer_type):
        """Sets the transformer_type of this Transformer.


        :param transformer_type: The transformer_type of this Transformer.  # noqa: E501
        :type: str
        """

        self._transformer_type = transformer_type

    @property
    def image(self):
        """Gets the image of this Transformer.  # noqa: E501


        :return: The image of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Transformer.


        :param image: The image of this Transformer.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def command(self):
        """Gets the command of this Transformer.  # noqa: E501


        :return: The command of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this Transformer.


        :param command: The command of this Transformer.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def args(self):
        """Gets the args of this Transformer.  # noqa: E501


        :return: The args of this Transformer.  # noqa: E501
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Transformer.


        :param args: The args of this Transformer.  # noqa: E501
        :type: str
        """

        self._args = args

    @property
    def resource_request(self):
        """Gets the resource_request of this Transformer.  # noqa: E501


        :return: The resource_request of this Transformer.  # noqa: E501
        :rtype: ResourceRequest
        """
        return self._resource_request

    @resource_request.setter
    def resource_request(self, resource_request):
        """Sets the resource_request of this Transformer.


        :param resource_request: The resource_request of this Transformer.  # noqa: E501
        :type: ResourceRequest
        """

        self._resource_request = resource_request

    @property
    def env_vars(self):
        """Gets the env_vars of this Transformer.  # noqa: E501


        :return: The env_vars of this Transformer.  # noqa: E501
        :rtype: list[EnvVar]
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        """Sets the env_vars of this Transformer.


        :param env_vars: The env_vars of this Transformer.  # noqa: E501
        :type: list[EnvVar]
        """

        self._env_vars = env_vars

    @property
    def created_at(self):
        """Gets the created_at of this Transformer.  # noqa: E501


        :return: The created_at of this Transformer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Transformer.


        :param created_at: The created_at of this Transformer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Transformer.  # noqa: E501


        :return: The updated_at of this Transformer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Transformer.


        :param updated_at: The updated_at of this Transformer.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Transformer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Transformer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transformer):
            return True

        return self.to_dict() != other.to_dict()
