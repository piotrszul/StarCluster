from fabric.api import run,sudo,env,execute, hosts
from fabric.operations import reboot,put
from fabric.contrib.files import contains, upload_template, exists
import os
import boto.s3.connection
import boto.ec2.connection
from boto.ec2.regioninfo import RegionInfo
from boto.s3.key import Key
import glob
from time import sleep


#Cloud specific constants
DEPLOY_HOST='115.146.94.144'
AWS_ACCESS_KEY='e59c100351844ab785ca5133905ec184'
AWS_SECRET_KEY='54f80f17fd4140f8b24b36906453195d'


def clean():
    os.system('rm -rf ./build')


def init():
    os.system('mkdir build')


def _get_s3_connection():
    return boto.s3.connection.S3Connection(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        port=8080,
        host='tascloud.it.csiro.au',
        is_secure=False,
        calling_format=boto.s3.connection.OrdinaryCallingFormat())
    
def _delete_bucket(bucket):
        for key in  bucket.list():
            print "Deleting %s" % key.name
            bucket.delete_key(key.name)
        bucket.delete()


def _get_ec2_connection():
    connection = boto.ec2.connection.EC2Connection(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        port=8773,
        region = RegionInfo(endpoint='tascloud.it.csiro.au'),
        path = '/services/Cloud',
        is_secure=False)
    return connection


def cloud_init():
    pass
        

def cloud_cleanup():
    connection = _get_ec2_connection()
    print "Terminating all instances"
    for res in connection.get_all_instances():
        for instance in res.instances:
            instance.terminate()        
    while 0 !=  len(connection.get_all_instances()):
        print "Waiting for all intances to terminate"
        sleep(5)
            

    print "Removing cluster security groups"
    for sg in connection.get_all_security_groups():
        if sg.name != 'default':
            sg.delete()
            

def cloud_info():
    connection = _get_ec2_connection()
    for res in connection.get_all_instances():
        for instance in res.instances:
            print instance
    print connection.get_all_volumes()
    for volume in connection.get_all_volumes():
        print volume, volume.attachment_state()
    
    print connection.get_all_snapshots()
    print connection.get_all_key_pairs()
    print connection.get_all_security_groups()
    for image in connection.get_all_images():
        print image, image.name


    
def _mount_volume(connection):
    volume_galaxy_tools = connection.get_all_volumes(['vol-00000006'])[0] 
    print volume_galaxy_tools.attachment_state()
    volume_galaxy_tools.attach('i-000002b0', '/dev/vdd')    
    volume_galaxy_tools.update()
    while 'attached' !=  volume_galaxy_tools.attachment_state():
        print "Waiting for a volume to get attached"
        sleep(5)
        volume_galaxy_tools.update()
    print volume_galaxy_tools.attachment_state()

def _umount_volume(connection):
    volume_galaxy_tools = connection.get_all_volumes(['vol-00000006'])[0] 
    volume_galaxy_tools.detach()    
    volume_galaxy_tools.update()
    while None !=  volume_galaxy_tools.attachment_state():
        print "Waiting for a volume to get detached"
        sleep(5)
        volume_galaxy_tools.update()
    print volume_galaxy_tools.attachment_state()



