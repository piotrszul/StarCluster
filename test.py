#!/usr/bin/python
import starcluster.userdata
import starcluster.sshutils

data = 'Content-Type: multipart/mixed; boundary="===============1496146817178696941=="\nMIME-Version: 1.0\n\n--===============1496146817178696941==\nContent-Type: text/x-shellscript; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nContent-Disposition: attachment; filename="_sc_aliases.txt"\n\n#!/bin/false\n#ignored\nmaster\nnode001\n--===============1496146817178696941==\nContent-Type: text/x-shellscript; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nContent-Disposition: attachment; filename="_sc_plugins.txt"\n\n#!/bin/false\n#ignored\neJzTyCkw5NIDAAWnAW4=\n\n--===============1496146817178696941==\nContent-Type: text/x-shellscript; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nContent-Disposition: attachment; filename="_sc_volumes.txt"\n\n#!/bin/false\n#ignored\neJwdyLsJgEAQBcD8VWIk+GlAsAIbWHQ9ZOHwjr23gd0rJhOMaqmPeLrwoeVu9FAWRx3QaePumqMx\neR+03LCQbkcwraZEHaEiR1im3SI4/5zQndzqjP4Finkhfg==\n\n--===============1496146817178696941==\nContent-Type: text/cloud-config; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nContent-Disposition: attachment; filename="starcluster_cloud_config.txt"\n\n#cloud-config\ndisable_root: 0\n--===============1496146817178696941==--'

#print starcluster.userdata.unbundle_userdata(data, False)

#                 host,
#                 username=None,
#                 password=None,
#                 private_key=None,
#                 private_key_pass=None,

sshutil = starcluster.sshutils.SSHClient('140.79.7.52', 'ubuntu', private_key='/home/ubuntu/.ssh/id_rsa')
sshutil.mkdir(path="/xxxxx",  ignore_failure=False)