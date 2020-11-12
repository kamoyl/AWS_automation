# AWS automation
AWS EC2, S3 and some other (lambda, SNS, CloudWatch, CloudTrail etc) automation scripts (deployment, cleaning, maintenance). the idea is to: run a script and have already fully defined, working environment with all needed services, and appropriately configured policies and secure groups... On the other hands to have a tool, to fully clean AWS AccoundID env.

Because it is a cloud environemnt and some things takes time (deployment of instance, instance being actually up, creating snapshot or image) - all commands are checking if resource is already available.

## prerequisites:
- already created VPC, IGW and subnet (usually defined by default, tested on newly created free tier account) - there is an assumptions they exist
- created IAM named profile - scripts won't run without providing profile name
- few initial VARIABLES:

## purpose

The main purpose of this repo is to - using only CLI, and as less as possible manual work - create automatically an environemnt for doing some tasks on the fly:
- create tight security group which only ads deployed IP and ssh protocol to access to EC2 instance(s)
- create policy
- create role
- attach role to policy
- create an instance profile
- add that role to instance profile
- create an EC2 instance based on an image (own images, but it is very easy to change it to standard one) - choosing the newest one if more
  - each instance when started notifies itself on slack channel
  - each instance when shut down - notifies itself on slack channel (services definitions are in the repo already)
- assign created instance profile to that instance
- assign security policy to the instance 
- create S3 bucket(s) with secure access and encrypted by default
- create a KeyPair - checking if there is already an ssh key of deployer to import it in case
  - use it in case there is something to do remotely
  - remote script functions are prepared to be deployed in background logging output, which is presented with the rest of output
- present details in nice output, with all monthly and annualy costs so far
- send appropriate notifications to slack channel - also nicely formatted
  - about costs
  - about own AMIs
  - about working/running instances
  - about volumes 

And also:
- clean the whole environment - if needed:
  - all instance profiles, roles, policies
  - all security groups
  - all instances
  - all volumes
  - all keypairs
  - leaving only own AMIs, and S3 buckets
  
## AWS extra addons

- SSM agent manual installation:
  - **[SSM rpm](https://s3.eu-west-1.amazonaws.com/amazon-ssm-eu-west-1/latest/linux_amd64/amazon-ssm-agent.rpm)**
  - ```aws ssm start-session --region=eu-west-1 --target [instance_id]```
- packages and configuration management: *cloudformation* or *terraform*
- reconfiguration ssh port to 2222:
  - (SELinux) ```semanage port -a -t ssh_port_t -p tcp 2222```

### AWS related links

- *[AWS info about policy versioning](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html)*
- *[automatic backup process EC2 -> S3](https://aws.amazon.com/blogs/startups/how-to-back-up-workloads-with-amazon-s3-ebs/)*
- *[Running commands on your Linux instance at launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)*
- *[How to use jq in oneliners AWS CLI](https://medium.com/circuitpeople/aws-cli-with-jq-and-bash-9d54e2eabaf1)*
- **[creating/attaching role to existing EC2 Instance](https://aws.amazon.com/blogs/security/new-attach-an-aws-iam-role-to-an-existing-amazon-ec2-instance-by-using-the-aws-cli/)**
- **[AWS Lambda - Launch EC2 Instances](https://medium.com/appgambit/aws-lambda-launch-ec2-instances-40d32d93fb58)**
- *[AWS Lambda - nice guide](https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide/)
- [s3fs - mounting s3 bucket as a filesystem under linux](https://github.com/s3fs-fuse/s3fs-fuse)
- [goofys - one of a method of mounting s3 as filesystem to linux](https://github.com/kahing/goofys)
- [sharing encrypted AMIs between accounts](https://aws.amazon.com/blogs/security/how-to-share-encrypted-amis-across-accounts-to-launch-encrypted-ec2-instances/)
### other
- *[slack emoji](https://www.webfx.com/tools/emoji-cheat-sheet)*
- *[markdown guide](https://www.markdownguide.org/basic-syntax)*
