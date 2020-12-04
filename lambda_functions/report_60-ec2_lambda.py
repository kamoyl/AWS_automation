import os
import boto3

ec2 = boto3.client('ec2', region_name='${REGION}')

def ${AWS_HANDLER_FUNCTION_NAME}(event, context):
  print('## ENVIRONMENT VARIABLES')
  print(os.environ)
  print('## EVENT')
  print(event)
  #message = event['message']
  #message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
  init_script = """#!/usr/bin/env bash
                sudo -u jenkins -i -- git clone -b master ssh://git@git.kpn.org:7999/ter/td-aws.git /var/lib/jenkins/td-aws > /tmp/td-aws_cloning.log 2>&1
                sudo -u jenkins -i -- git clone -b 8.0.0 ssh://git@git.kpn.org:7999/ter/td-monitoring.git /var/lib/jenkins/td-monitoring > /tmp/td-monitoring_cloning.log 2>&1
                sudo -u jenkins -i -- cd /var/lib/jenkins/td-monitoring
                sudo -u jenkins -i -- /var/lib/jenkins/td-monitoring/report_generator -n 60 -s DTA -o /var/lib/jenkins/td-monitoring/var_report_DTA_60 > /tmp/report_60_DTA.log 2>&1
                sudo -u jenkins -i -- /var/lib/jenkins/td-monitoring/report_generator -n 907 -s DTA -o /var/lib/jenkins/td-monitoring/var_report_DTA_60 > /tmp/report_60_DTA.log 2>&1
                """

  instance = ec2.run_instances(
      KeyName='${KEY_NAME}',
      ImageId='${LATEST_AMI_ID}',
      InstanceType='${AWS_INSTANCE_TYPE}',
      SubnetId='${SUBNET_ID}',
      MaxCount=1,
      MinCount=1,
      InstanceInitiatedShutdownBehavior='terminate',
      Monitoring={
        'Enabled': True
        },
      IamInstanceProfile={
        'Name': '${AWS_EC2_INSTANCES_PROFILE}'
      },
      SecurityGroupIds=[
        '${SECURITY_GROUP_ID}'
        ],
      BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'DeleteOnTermination': True
              }
          },
      ],
      UserData=init_script
    )

  instance_id = instance['Instances'][0]['InstanceId']
  print(instance_id)

  return instance_id
