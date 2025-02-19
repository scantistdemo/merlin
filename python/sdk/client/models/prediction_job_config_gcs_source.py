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


class PredictionJobConfigGcsSource(object):
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
        'format': 'FileFormat',
        'uri': 'str',
        'features': 'list[str]',
        'options': 'dict(str, str)'
    }

    attribute_map = {
        'format': 'format',
        'uri': 'uri',
        'features': 'features',
        'options': 'options'
    }

    def __init__(self, format=None, uri=None, features=None, options=None, _configuration=None):  # noqa: E501
        """PredictionJobConfigGcsSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._format = None
        self._uri = None
        self._features = None
        self._options = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if uri is not None:
            self.uri = uri
        if features is not None:
            self.features = features
        if options is not None:
            self.options = options

    @property
    def format(self):
        """Gets the format of this PredictionJobConfigGcsSource.  # noqa: E501


        :return: The format of this PredictionJobConfigGcsSource.  # noqa: E501
        :rtype: FileFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PredictionJobConfigGcsSource.


        :param format: The format of this PredictionJobConfigGcsSource.  # noqa: E501
        :type: FileFormat
        """

        self._format = format

    @property
    def uri(self):
        """Gets the uri of this PredictionJobConfigGcsSource.  # noqa: E501


        :return: The uri of this PredictionJobConfigGcsSource.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this PredictionJobConfigGcsSource.


        :param uri: The uri of this PredictionJobConfigGcsSource.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def features(self):
        """Gets the features of this PredictionJobConfigGcsSource.  # noqa: E501


        :return: The features of this PredictionJobConfigGcsSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this PredictionJobConfigGcsSource.


        :param features: The features of this PredictionJobConfigGcsSource.  # noqa: E501
        :type: list[str]
        """

        self._features = features

    @property
    def options(self):
        """Gets the options of this PredictionJobConfigGcsSource.  # noqa: E501


        :return: The options of this PredictionJobConfigGcsSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PredictionJobConfigGcsSource.


        :param options: The options of this PredictionJobConfigGcsSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

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
        if issubclass(PredictionJobConfigGcsSource, dict):
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
        if not isinstance(other, PredictionJobConfigGcsSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredictionJobConfigGcsSource):
            return True

        return self.to_dict() != other.to_dict()
