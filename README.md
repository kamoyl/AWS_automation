# AWS_automation
AWS EC2, S3 and some other (lambda, SNS, CloudWatch etc) automation scripts (deployment, cleaning, maintenance)
## purpose

The main purpose of this repo is to - using only CLI, and as less as possible manual work - create automatically an environemnt for doing some tasks on the fly:
- create tight security group which only ads deployed IP and ssh protocol to access to EC2 instance(s)
- create policy
- create role
- attach role to policy
- create an instance profile
- add that role to instance profile
- create an EC2 instance based on an image (own images, but it is very easy to change it to standard one) - choosing the newest one if more
- assign created instance profile to that instance
- assign security policy to the instance 
- create S3 bucket(s) with secure access and encrypted by default
- create a KeyPair - checking if there is already an ssh key of deployer to import it in case
- present details in nice output, with all monthly and annualy costs so far
