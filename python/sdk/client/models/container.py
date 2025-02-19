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


class Container(object):
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
        'name': 'str',
        'pod_name': 'str',
        'component_type': 'str',
        'namespace': 'str',
        'cluster': 'str',
        'gcp_project': 'str',
        'version_endpoint_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'pod_name': 'pod_name',
        'component_type': 'component_type',
        'namespace': 'namespace',
        'cluster': 'cluster',
        'gcp_project': 'gcp_project',
        'version_endpoint_id': 'version_endpoint_id'
    }

    def __init__(self, name=None, pod_name=None, component_type=None, namespace=None, cluster=None, gcp_project=None, version_endpoint_id=None, _configuration=None):  # noqa: E501
        """Container - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._pod_name = None
        self._component_type = None
        self._namespace = None
        self._cluster = None
        self._gcp_project = None
        self._version_endpoint_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if pod_name is not None:
            self.pod_name = pod_name
        if component_type is not None:
            self.component_type = component_type
        if namespace is not None:
            self.namespace = namespace
        if cluster is not None:
            self.cluster = cluster
        if gcp_project is not None:
            self.gcp_project = gcp_project
        if version_endpoint_id is not None:
            self.version_endpoint_id = version_endpoint_id

    @property
    def name(self):
        """Gets the name of this Container.  # noqa: E501


        :return: The name of this Container.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Container.


        :param name: The name of this Container.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pod_name(self):
        """Gets the pod_name of this Container.  # noqa: E501


        :return: The pod_name of this Container.  # noqa: E501
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this Container.


        :param pod_name: The pod_name of this Container.  # noqa: E501
        :type: str
        """

        self._pod_name = pod_name

    @property
    def component_type(self):
        """Gets the component_type of this Container.  # noqa: E501


        :return: The component_type of this Container.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this Container.


        :param component_type: The component_type of this Container.  # noqa: E501
        :type: str
        """
        allowed_values = ["image_builder", "model", "transformer", "batch_job_driver", "batch_job_executor"]  # noqa: E501
        if (self._configuration.client_side_validation and
                component_type not in allowed_values):
            raise ValueError(
                "Invalid value for `component_type` ({0}), must be one of {1}"  # noqa: E501
                .format(component_type, allowed_values)
            )

        self._component_type = component_type

    @property
    def namespace(self):
        """Gets the namespace of this Container.  # noqa: E501


        :return: The namespace of this Container.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Container.


        :param namespace: The namespace of this Container.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def cluster(self):
        """Gets the cluster of this Container.  # noqa: E501


        :return: The cluster of this Container.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Container.


        :param cluster: The cluster of this Container.  # noqa: E501
        :type: str
        """

        self._cluster = cluster

    @property
    def gcp_project(self):
        """Gets the gcp_project of this Container.  # noqa: E501


        :return: The gcp_project of this Container.  # noqa: E501
        :rtype: str
        """
        return self._gcp_project

    @gcp_project.setter
    def gcp_project(self, gcp_project):
        """Sets the gcp_project of this Container.


        :param gcp_project: The gcp_project of this Container.  # noqa: E501
        :type: str
        """

        self._gcp_project = gcp_project

    @property
    def version_endpoint_id(self):
        """Gets the version_endpoint_id of this Container.  # noqa: E501


        :return: The version_endpoint_id of this Container.  # noqa: E501
        :rtype: int
        """
        return self._version_endpoint_id

    @version_endpoint_id.setter
    def version_endpoint_id(self, version_endpoint_id):
        """Sets the version_endpoint_id of this Container.


        :param version_endpoint_id: The version_endpoint_id of this Container.  # noqa: E501
        :type: int
        """

        self._version_endpoint_id = version_endpoint_id

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
        if issubclass(Container, dict):
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
        if not isinstance(other, Container):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Container):
            return True

        return self.to_dict() != other.to_dict()
