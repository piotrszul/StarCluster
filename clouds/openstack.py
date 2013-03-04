'''
Created on Feb 28, 2013

@author: ubuntu
'''

import boto.ec2.connection
import fnmatch
from IPython.config.application import catch_config_error



def connect_ec2(aws_access_key_id=None, aws_secret_access_key=None, **kwargs):
    """
    :type aws_access_key_id: string
    :param aws_access_key_id: Your AWS Access Key ID

    :type aws_secret_access_key: string
    :param aws_secret_access_key: Your AWS Secret Access Key

    :rtype: :class:`boto.ec2.connection.EC2Connection`
    :return: A connection to Amazon's EC2
    """
    return EC2Connection(aws_access_key_id, aws_secret_access_key, **kwargs)

class EC2Connection(boto.ec2.connection.EC2Connection):
    def __init__(self, *args, **kwargs):
        super(EC2Connection, self).__init__(*args, **kwargs)
        print "Initializing openstack connection"

    
    def create_tags(self, resource_ids, tags):
        print "create tags not supported %s:%s" % (resource_ids, tags)

    def delete_tags(self, resource_ids, tags):
        print "delete tagd not supported %s:%s" % (resource_ids, tags)

    def get_all_security_groups(self, groupnames=None, group_ids=None, filters=None):
        try:
            sgs =  boto.ec2.connection.EC2Connection.get_all_security_groups(self, groupnames=groupnames, group_ids=group_ids, filters=filters)
            print sgs.__class__
            if filters !=None and filters.get('group-name')!=None:
                glob = filters.get('group-name')
                sgs = filter(lambda sg: fnmatch.fnmatchcase(sg.name, glob), sgs)
            return sgs
        except boto.exception.EC2ResponseError, e:
            if e.error_code == "SecurityGroupNotFoundForProject":
                e.error_code = "InvalidGroup.NotFound"
                raise e
            raise


    def get_all_instances(self, instance_ids=None, filters=None):
        if filters != None:
            print("Warning instance filters not supported %s" % filters )
        reservations = boto.ec2.connection.EC2Connection.get_all_instances(self, instance_ids=instance_ids, filters=filters)
        for r in reservations:
            for i in r.instances:
                i.groups = r.groups
                for g in i.groups:
                    g.name = g.id
        return reservations

#fnmatch.fnmatchcase


class EC2DelegateConnection(object):
    '''
    classdocs
    '''
    def __init__(self, boto_connection):
        self._boto_connection = boto_connection


    def __getattr__(self, name):
        return self._boto_connection.__getattribute__(name)
        
    def get_all_security_groups(self, **kwargs):
        print "Asked for security groups %s" % kwargs
        return self._boto_connection.get_all_security_groups(**kwargs)
    
    def xx(self):
        self._boto_connection.set_tags()