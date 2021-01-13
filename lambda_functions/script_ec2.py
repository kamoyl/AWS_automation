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
  init_script = """${SHELL_SCRIPT}"""

  instance = ec2.run_instances(
      KeyName='${KEY_NAME}',
      ImageId='${AWS_AMI_ID}',
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
