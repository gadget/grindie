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

run_instances() {
  echo "Starting EC2 instances"
  # FIXME: simple startup of 2 instances with hardcoded ami and keypair for testing purposes
  ec2-run-instances ami-8c1fece5 -k adam.dobos -n 2
  ec2-authorize default -p 22

  echo -n "Waiting for instances to boot"
  # FIXME: wait for 2 instances to boot and go on
  instCnt=0
  while [ $instCnt -lt 2 ]
  do
    sleep 2s
    instCnt=`ec2-describe-instances |grep running |grep INSTANCE |wc -l`
    echo -n "."
  done
}

register_instances() {
  echo -e "\nRegistering instances"
  rm -f settings/cloud.instances
  idx=0
  ec2-describe-instances |grep running |grep INSTANCE |cut -f2,4 |while read inst
  do
    echo -e "inst$idx\t$inst" >> settings/cloud.instances
    let idx++
  done
}

prepare_scenario() {
  echo "Preparing scenario to run in EC2"
  # TODO: implement
}

run_instances
register_instances
prepare_scenario

echo -e "Done.\n"
exit 0
