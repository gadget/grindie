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

. ./common.sh

usage() {
  echo -e "Usage: $0 [options]\n\nOptions:"
  echo "  -k keypair (required)"
  echo "  -g security group"
  echo "  -a ami id"
}

SETTINGS_CLOUD="settings/cloud.instances"
SETTINGS_SCENARIO="settings/scenario.conf"
SETTINGS_SCENARIO_TMP="settings/scenario.conf.tmp"

KEYPAIR=
GROUP="default"
AMI_ID="ami-43477e37"

E_INVALID_OPTION=101
while getopts "hk:g:a:" OPTION
do
  case $OPTION in
    h) usage; exit 0;;
    k) KEYPAIR=$OPTARG;;
    g) GROUP=$OPTARG;;
    a) AMI_ID=$OPTARG;;
    ?) usage; exit $E_INVALID_OPTION;;
  esac
done

E_NO_KEYPAIR=102
if [ -z $KEYPAIR ]
then
  usage
  exit $E_NO_KEYPAIR
fi

# the required number of EC2 instances to run the scenario
NUM_OF_INSTANCES=`cat $SETTINGS_SCENARIO |grep -v '#' |grep -v "^$" |cut -d" " -f1 |sort |uniq |wc -l`

run_instances() {
  echo -e "\nStarting $NUM_OF_INSTANCES EC2 instances"
  ec2-run-instances $AMI_ID -g $GROUP -k $KEYPAIR -n $NUM_OF_INSTANCES > ec2-run-instances.out 2> ec2-run-instances.err
  check_ret

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
  # creating a mapping file with logical identifiers and actual hosts of the EC2 instances
  # e.g. 'inst0   i-e97dd79f      ec2-46-137-3-225.eu-west-1.compute.amazonaws.com'
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
  # replacing logical identifiers in the scenario by actual hosts using the previously created mapping file
  echo "Preparing scenario to run in EC2"
  awk 'NR==FNR{map[$1]=$3;next} {if (length($1)>0 && substr($1,1,1)!="#" && length(map[$1])>0) {$1=map[$1]}}1' $SETTINGS_CLOUD $SETTINGS_SCENARIO > $SETTINGS_SCENARIO_TMP && mv $SETTINGS_SCENARIO_TMP $SETTINGS_SCENARIO
  check_ret
}

run_instances
register_instances
prepare_scenario

echo -e "Done.\n"
exit 0
