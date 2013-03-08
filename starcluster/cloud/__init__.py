from starcluster import awsutils, exception
from starcluster.cloud import openstack

class CloudFactory(object):
    
    def get_easy_ec2(self):
        pass

    def get_easy_s3(self):
        pass

    @staticmethod
    def get(config):
        return OpenStackCloudFactory(config)
 
class AWSCloudFactory(CloudFactory):

    def __init__(self, config):
        self._config = config

    def get_easy_ec2(self):
        aws = self._config.get_aws_credentials()
        try:
            ec2 = awsutils.EasyEC2(**aws)
            return ec2
        except TypeError:
            raise exception.ConfigError("no aws credentials found")

    def get_easy_s3(self):
        pass
    
    
class OpenStackCloudFactory(CloudFactory):

    def __init__(self, config):
        self._config = config

    def get_easy_ec2(self):
        aws = self._config.get_aws_credentials()
        aws['connection_authenticator'] = openstack.connect_ec2
        try:
            ec2 = awsutils.EasyEC2(**aws)
            return ec2
        except TypeError:
            raise exception.ConfigError("no aws credentials found")

    def get_easy_s3(self):
        pass    
        