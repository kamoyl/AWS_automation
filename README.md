# AWS automation
AWS EC2, S3 and some other (lambda, SNS, CloudWatch, CloudTrail etc) automation scripts (deployment, cleaning, maintenance). the idea is to: run a script and have already fully defined, working environment with all needed services, and appropriately configured policies and secure groups... On the other hands to have a tool, to fully clean AWS AccoundID env.

Because it is a cloud environemnt and some things takes time (deployment of instance, instance being actually up, creating snapshot or image) - all commands are checking if resource is already available.

It works both: in hybrid clouds, and in public one either (I tested it against [CloudGuru sandboxes](https://learn.acloud.guru/cloud-playground/cloud-sandboxes) and it works fine (despite some restriction which is described on CloudGuru site).

Scripts takes care for permissions, relations (to entities) and support error handling; the funniest is that from the scripts and CLI you may collect much more information then AWS console...

Which also means, and it is nice advere effect, that running just info - it collects all information about current env of an AccountAD - with all extra created policies, roles, or other entities, and lots more that that - the most interested it is when run aws_info script against just created CloudGuru sandbox :)

## prerequisites:
- some more-or-less obvious tools: ip, ifconfig, bc, and [grepcidr](http://www.pc-tools.net/unix/grepcidr/)
- already created VPC, IGW and subnet (usually defined by default, tested on newly created free tier account) - there is an assumptions they exist
- created IAM named profile - scripts won't run without providing profile name
- few initial mandatory VARIABLES (they are mostly covered, but they are personal):
  - ```AWS_DEFAULT_NAME``` - for prefixing security groups, policies, roles, instance profiles etc
  - ```AWS_COMMON_NAME``` - for prefixing something "bigger", and for more then one person/instance, like S3 buckets
  - ```AWS_NETWORK_TAG``` - in case there are some TAGs/Names of particular networks (like: private), if empty, then all taken
  - ```AWS_REPO_ADDRESS="https://kamoyl.github.io/AWS_automation/"``` (it is already pointing [here](https://kamoyl.github.io/AWS_automation/), because this repo is cloned on newly created instance and from that repo, and that instance there is a possibility to manage the AWS env also (policy is already properly created)
  - ```SLACK_CHANNEL_AWS```
  - ```SLACK_WEB_HOOK``` (for sending notifications about status of volumes and instances etc)
  - ```SLACK_TOKEN```
- parameters needed:
  - ```DEPLOY_USER``` (-u) - user which have permissions to do what we need to be done on created instance (optional parameter, default: "jenkins")
  - ```AWS_PROFILE``` (-p) - profile with which all commands (AWS CLI) will be run (mandatory parameter)
  - ```AWS_AMI_ID```  (-A) - AMI ID (when there is no local AMI(s)) (optional parameter, by default scripts are trying to figure it out from local AMI(s) which is the newest (created as the latest)
  - ```AWS_INSTANCE_TYPE``` (-I) - optional parameter (default is free tier: "t3.small")
  
## purpose

The main purpose of this repo is to - using only CLI, and as less as possible manual work - create automatically an environemnt for doing some tasks on the fly:
- create tight security group which only ads deployed IP and ssh protocol to access to EC2 instance(s) (only when instance is created)
- create common policy group which adds a group of networks with ssh protocol to access to EC2 instance(s) created by lambda
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
- very simmilar process is done when creating a lambda function which deployes EC2 instance based on delivered image ID (or pick up own newest) and runs appropriate code (of course with different policies, groups etc)
- present details in nice output, with all monthly and annualy costs so far
- CloudTrail (ToDo)
- events (busses, rules etc) - for appropriately deploy and run EC2 with a code, and clean environment afterword
- send appropriate notifications to slack channel - also nicely formatted
  - about costs
  - about own AMIs
  - about working/running instances
  - about volumes
  - S3 buckets (and their features: lifecycle, encryption, secure access etc)
- created instances (doesn't matter if by Lambda or directly) are deployed with 

And also:
- clean the whole environment - if needed:
  - all instance profiles, roles, policies
  - all security groups
  - all instances
  - all volumes
  - all keypairs
  - leaving only own AMIs, and S3 buckets

## parameters:

Each script without any parameter will throw help, but:
### aws_info
  - [-o]  OUTPUT directory - where to store ALL LOGs and TEMP files (default directory is: /${HOME}/var and TMP and LOG are subdirectories to var)
  - [-p]  [mandatory outside AWS env] - PROFILE name stored in ~/.aws/config
  - [-C]  CLEANING (WARNING) - removing all running/stopped instance(s) (terminates them) and all volumes and snapshots
  - [-x]  only works with [-C] - CLEANING (WARNING) - removes: S3 buckets (only empty), Lambda functions, events-busses etc., event rules, Keys etc
  - [-v]  verbose
###aws_deploy
  - those from aws_info except [-C] and [-x]
  - [-E]  deployment of EC2 instance
  - [-L]  deployment of Lambda function with EventBridge schedule
  - [-u]  [optional] - username on remote system which runs commands (if ommited, then "${USER}" is picked up)
  - [-R]  [optional] - run code remotely on just created EC2 instance
  - [-A]  [optional] - AMI_ID         (if ommited, then the newest OWN is picked up)
    - example: Red Hat Enterprise Linux 8 (HVM), SSD Volume Type (ami-032e5b6af8a711f30) - for eu-west-1 AZ
    - example: Amazon Linux 2 AMI (HVM), SSD Volume Type (ami-0ce1e3f77cd41957e) - for eu-west-1 AZ
    - example: CentOS 7 (x86_64) - with Updates HVM (ami-05a178e6f938f2c39) - for eu-west-1 AZ
    - example of find: "aws --profile saml ec2 describe-images --filters "Name=description,Values=CentOS 7*" | jq '.Images[].Description'"
  - [-I]  [optional] - INSTANCE_TYPE  (if ommited, then "t3.xlarge" is picked up)
 
## AWS extra addons

- SSM agent manual installation:
  - **[SSM rpm](https://s3.eu-west-1.amazonaws.com/amazon-ssm-eu-west-1/latest/linux_amd64/amazon-ssm-agent.rpm)**
  - ```aws ssm start-session --region=eu-west-1 --target [instance_id]```
- packages and configuration management: *cloudformation* or *terraform*
- reconfiguration ssh port to 2222:
  - (SELinux) ```semanage port -a -t ssh_port_t -p tcp 2222```

### AWS related links
- [AWS cli installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
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

* __* updated Public IP entry__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 14 Jan 2021 16:13:40 +0100
    
    * permi^Cions to logging and logging enabling to bucket is enabled and set
    properly
    
    * taking care for security groups not needed during removing/terminating
    instances
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 14 Jan 2021 12:46:16 +0100
    
    

* __Added buckets logging__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 14 Jan 2021 12:42:49 +0100
    
    * preparation for buckets objects locking
    

* __Updated README__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 13 Jan 2021 13:24:58 +0100
    
    

* __Changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 13 Jan 2021 13:16:11 +0100
    
    

* __* lambda name has been changed to be used more then one - accordingly to destination scripts__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 13 Jan 2021 13:13:45 +0100
    
    * configuration table is now three columns where two of them are lambda pythin
    script and bash script runs by it
    
    * there were lots of weirdissues related to IFS - which all of them is globally
    corrected now
    
    * more and more redirection to logs and temporary files accordingly if it is
    about output or errors
    
    * corrected OpenSSH fingerprint comparison to AWS SSH2 fingerptint - to NOT to
    create endlesly keys if they exists already
    
    * added ToDo into README and update it
    
    * checking if: ** event is already created, ** if permissions from EventBridge
    to Lambda are appropriately assigned and created, ** event name is uniq, ** if
    event rule is already created, ** if targets exists
    
    * changed orger of creating zip package for lambda to do it ONLY after creating
    lambda
    
    * updated README, and Changelog
    
    * some small changes and cleaning
    

* __Changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 7 Jan 2021 21:27:58 +0100
    
    

* __* slow change to separation error logs from output files__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 7 Jan 2021 21:26:25 +0100
    
    * added permissions and trust to events for run lambda function
    
    * corrected output file which overwrites event rules
    

* __* slow change to separation error logs from output files__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 7 Jan 2021 21:21:01 +0100
    
    

* __Changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 6 Jan 2021 16:18:50 +0100
    
    

* __* slow change to separation error logs from output files__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 6 Jan 2021 15:59:12 +0100
    
    

* __* added slack notification to deployment of lambda, target and event rule__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 6 Jan 2021 14:14:22 +0100
    
    * few small changes
    

* __* separated some output files from error files when output is redirected__

    [Kamil Czarnecki](kamoyl@outlook.com) - Tue, 5 Jan 2021 16:39:25 +0100
    
    * added lambda proper deployment slack notification
    

* __Changed slack proxy parameters to array due to missunderstanding of dashes in variable__

    [Kamil Czarnecki](kamoyl@outlook.com) - Mon, 4 Jan 2021 15:29:16 +0100
    
    corrected IFS when slack is called - due to improper caret
    

* __Changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Sat, 12 Dec 2020 21:23:12 +0100
    
    * updated README
    

* __Small notification change__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 11 Dec 2020 16:15:20 +0100
    
    

* __* corrected issue with inapropriately checking subnets without tags__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 11 Dec 2020 16:14:18 +0100
    
    * due to TIME needed to initiate an instance, and then assigning profile - I
    had to add a progress bar UNTIL instance will be running
    

* __few correction and few checkes to do smoothly through__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 10 Dec 2020 21:37:36 +0100
    
    

* __Lots of changes__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 10 Dec 2020 17:08:50 +0100
    
    * checking if permissions are in place, if not - some tasks cannot be finished
    but error must be handled
    
    * some tasks is not possible to do, errror handling added
    
    * in some cases there are unremovable relation to entities - which cannot - due
    to permissions - be removed - error handling
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 10 Dec 2020 16:40:52 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 10 Dec 2020 12:30:24 +0100
    
    

* __Changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 9 Dec 2020 16:50:57 +0100
    
    

* __* all scripts are prepared now to be run outside AWS instance, and from it either - it means that cleaning is safe (current instance will be untouched, so as policied, secure groups, etc), profile is taken properly frmo inside EC2 instance and from autiside__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 9 Dec 2020 16:49:09 +0100
    
    * added lifecycle to S3 buckets
    
    * optimize a bit - run in parallel with shortened time about half
    

* __* updated gitignore__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 9 Dec 2020 10:52:52 +0100
    
    * added some - useful I think - scripts for EC2 instance to deploy - it is even
    easy to do it by lambda when creating an instance of by deploying a script when
    deploying instance on the fly
    
    * added: zram configuration (useful with small instances), and slack
    notification WHEN vm is up, and when it is going down - based on systemd
    

* __* adding changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 9 Dec 2020 10:12:23 +0100
    
    

* __* small correction of static value when sending slack__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 9 Dec 2020 10:11:08 +0100
    
    

* __* added checking of S3 buckets features like secure access instead of apply it each time__

    [Kamil Czarnecki](kamoyl@outlook.com) - Tue, 8 Dec 2020 16:39:53 +0100
    
    * Lambda and Evens are now taken from one filke, with schedule, so it shhould
    be easier then it was
    

* __* lambda is migrated to bash function, which let&#39;s now deploy more of them, related to evens by name__

    [Kamil Czarnecki](kamoyl@outlook.com) - Mon, 7 Dec 2020 16:57:07 +0100
    
    

* __* Added changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 4 Dec 2020 16:11:24 +0100
    
    

* __* Added changelog__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 4 Dec 2020 16:09:57 +0100
    
    

* __* eventbridge attached - it is deployed right after lambda, and with lambda related__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 4 Dec 2020 16:04:15 +0100
    
    * few correction to lambda deployment
    
    * changed picking up lambda scripts - now each one in lambda_functions with .py
    extension will be picked up, and based on it, appropriate event will be created
    

* __* added checking mandatory aws cli__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 4 Dec 2020 14:38:22 +0100
    
    * aws cli version is also checked
    
    * added an aws cli installation link to README
    

* __Add scripts - init of a branch__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 4 Dec 2020 12:40:51 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 2 Dec 2020 13:10:55 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Mon, 16 Nov 2020 12:14:11 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Mon, 16 Nov 2020 10:29:22 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 13 Nov 2020 10:43:50 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 16:38:02 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 16:36:41 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 14:22:06 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 14:21:31 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 11:55:12 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 11:50:45 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 11:36:15 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 10:13:56 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 09:42:19 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 12 Nov 2020 09:26:48 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 11 Nov 2020 13:07:38 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 11 Nov 2020 09:32:03 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 11 Nov 2020 09:24:59 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Wed, 11 Nov 2020 09:24:42 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Tue, 10 Nov 2020 12:41:11 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Tue, 10 Nov 2020 12:35:31 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Fri, 6 Nov 2020 13:56:52 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 5 Nov 2020 15:47:50 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 5 Nov 2020 15:42:08 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 5 Nov 2020 12:33:53 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 5 Nov 2020 12:25:49 +0100
    
    

* __Update README.md__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 5 Nov 2020 12:18:15 +0100
    
    

* __Initial commit__

    [Kamil Czarnecki](kamoyl@outlook.com) - Thu, 5 Nov 2020 12:13:10 +0100
    
    
    

