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

SCRIPTS_HOME="/root/AWS_automation"
PARAMETERS=$(echo "$@" | sed 's/\-l .//g')
RANDOM_ID=$(cat /dev/urandom | tr -dc '0-9a-zA-Z' | fold -w 4 | head -n1)
VAR="/root/var"
TMP="/root/var/tmp"
LOG="/root/var/log"
mkdir -p ${VAR} ${TMP} ${LOG}

if [ -d /root/AWS_automation ]
then
  rm -rf /root/AWS_automation
  git clone -b master https://github.com/kamoyl/AWS_automation /root/AWS_automation > /tmp/td-aws_cloning.log 2>&1
else
  git clone -b master https://github.com/kamoyl/AWS_automation /root/AWS_automation > /tmp/td-aws_cloning.log 2>&1
fi

yum check-update
yum -y update
sync

cd /root/AWS_automation
source /root/AWS_automation/config
DESCRIPTION="${AWS_DEFAULT_NAME}_automaticly_created_with_updates"
aws_AMI_create ${LOCAL_EC2_INSTANCE} ${AWS_DEFAULT_NAME}_${RANDOM_ID} ${DESCRIPTION}
rm -rf /root/AWS_automation/td-aws

sync
