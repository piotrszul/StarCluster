#!/usr/bin/python
import boto.ec2.connection
from boto.ec2.regioninfo import RegionInfo


#e59c100351844ab785ca5133905ec184
#AWS_SECRET_ACCESS_KEY=54f80f17fd4140f8b24b36906453195d

connection = boto.ec2.connection.EC2Connection(
    aws_access_key_id='e59c100351844ab785ca5133905ec184',
    aws_secret_access_key='54f80f17fd4140f8b24b36906453195d',
    port=8773,
    region = RegionInfo(endpoint='tascloud.it.csiro.au'),
    path = '/services/Cloud',
    is_secure=False)


for res in connection.get_all_instances():
    for inst in res.instances:
        print inst
        
print connection.get_all_volumes()
print connection.get_all_snapshots()
print connection.get_all_key_pairs()
print connection.get_all_security_groups()

for image in connection.get_all_images():
    print image, image.name


print connection.get_instance_attribute('i-0000031d', 'userData')


print connection.get_all_instances(filters = {'instance_id': 'i-0000031d'})



