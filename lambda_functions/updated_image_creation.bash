#!/usr/bin/env bash

if [[ "${OSTYPE}" =~ "linux" ]]
then
  SCRIPT=$(readlink -f "$0")
elif [[ "${OSTYPE}" =~ "darwin" ]]
then
  SCRIPT=$(greadlink -f "$0")
else
  SCRIPT=$(readlink -f "$0")
fi

SCRIPTS_HOME=$(dirname "${SCRIPT}")

PARAMETERS=$(echo "$@" | sed 's/\-l .//g')

if [ -d /root/AWS_automation ]
then
  rm -rf /root/AWS_automation
  git clone -b master https://github.com/kamoyl/AWS_automation.git /root/AWS_automation
else
  git clone -b master https://github.com/kamoyl/AWS_automation.git /root/AWS_automation
fi

yum check-update
yum -y update
sync

source /root/AWS_automation/config
source /root/AWS_automation/config_aws
aws_AMI_create ${LOCAL_EC2_INSTANCE} ${AWS_DEFAULT_NAME}_${RANDOM_ID}
#aws_newest_ami

sync
shutdown -h now
