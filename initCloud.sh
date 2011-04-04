#
# Copyright 2010 Adam Dobos
#
# This file is part of Grindie.
#
# Grindie is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Grindie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Grindie.  If not, see <http://www.gnu.org/licenses/>.
#

#!/bin/sh

SETTINGS_CLOUD="settings/cloud.instances"
SETTINGS_SCENARIO="settings/scenario.conf"
SETTINGS_SCENARIO_TMP="settings/scenario.conf.tmp"

KEYPAIR=$1
AMI_ID=${2:-"ami-b1497ec5"}

E_USAGE=101
if [ -z $KEYPAIR ] || [ "$KEYPAIR" = "-h" ] || [ "$KEYPAIR" = "--help" ]
then
  echo -e "Usage: ./initCloud.sh [keypair [ami_id]]\n"
  exit $E_USAGE
fi

NUM_OF_INSTANCES=`cat $SETTINGS_SCENARIO |grep -v '#' |grep -v "^$" |cut -d" " -f1 |sort |uniq |wc -l`

run_instances() {
  echo -e "\nStarting $NUM_OF_INSTANCES EC2 instances"
  ec2-run-instances $AMI_ID -k $KEYPAIR -n $NUM_OF_INSTANCES > ec2-run-instances.out 2> ec2-run-instances.err
  ec2-authorize default -p 22 > ec2-authorize.out 2> ec2-authorize.err

  echo -n "Waiting for instances to boot"
  instCnt=0
  while [ $instCnt -lt $NUM_OF_INSTANCES ]
  do
    sleep 2s
    instCnt=`ec2-describe-instances |grep running |grep INSTANCE |wc -l`
    echo -n "."
  done
}

register_instances() {
  echo -e "\nRegistering instances"
  rm -f $SETTINGS_CLOUD
  idx=0
  ec2-describe-instances |grep running |grep INSTANCE |cut -f2,4 |while read inst
  do
    echo -e "inst$idx\t$inst" >> $SETTINGS_CLOUD
    let idx++
  done
}

prepare_scenario() {
  echo "Preparing scenario to run in EC2"
  awk 'NR==FNR{map[$1]=$3;next} {if (length($1)>0 && substr($1,1,1)!="#" && length(map[$1])>0) {$1=map[$1]}}1' $SETTINGS_CLOUD $SETTINGS_SCENARIO > $SETTINGS_SCENARIO_TMP && mv $SETTINGS_SCENARIO_TMP $SETTINGS_SCENARIO
}

run_instances
register_instances
prepare_scenario

echo -e "Done.\n"
exit 0
