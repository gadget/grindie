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

. ./settings/agentProps.sh
. ./common.sh

DATE_SUFFIX=`date +%Y-%m-%d_%H:%M:%S`
BACKUP_FILE="logs/backup_$DATE_SUFFIX.zip"

process_host() {
  host=$1
  echo "Gathering logs from $host"

  # create local temp directory for each host
  mkdir -p logs/$host/tmp
  check_ret

  # create a zip package with all the logs on remote agent
  ssh -n -i $AGENT_KEY $AGENT_USER@$host eval "'cd $AGENT_DIR/testcases; zip -rq logs.zip . -i \*log\*'"
  check_ret

  # download the newly created zip from agent to local temp directory
  scp -q -i $AGENT_KEY $AGENT_USER@$host:$AGENT_DIR/testcases/logs.zip logs/$host/tmp
  check_ret

  # delete the zip package on remote agent
  ssh -n -i $AGENT_KEY $AGENT_USER@$host eval "'rm $AGENT_DIR/testcases/logs.zip'"
  check_ret

  # extract the zip package in local temp directory
  unzip -q logs/$host/tmp/logs.zip -d logs/$host/tmp
  check_ret

  # iterate over testcase directories and move all the logs outside of temp directory
  # each log file needs to be renamed with a suffix of the current testcase name to
  # ensure that log files from different testcase directories won't overwrite each other
  cd logs/$host/tmp
  for testcase in *; do
    if [ -d $testcase ]
    then
      cd $testcase/log
      for logFile in *; do
        mv $logFile ../../../$logFile.$testcase
        check_ret
      done
      cd ../..
    fi
  done

  # finally we can delete the local temp directory
  cd ../../..
  rm -r logs/$host/tmp
  check_ret
}

echo "Creating backup of previously gathered logs: $BACKUP_FILE"
zip -rmq $BACKUP_FILE logs -x \*.zip
check_ret

echo -e "Gathering logs from agent machines with user: $AGENT_USER\n"

iterate_over_hosts process_host

echo -e "Done.\n"
exit 0
