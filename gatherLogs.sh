#!/bin/sh

. ./settings/agentProps.sh

DATE_SUFFIX=`date +%Y-%m-%d_%H:%M:%S`
BACKUP_FILE="logs/backup_$DATE_SUFFIX.zip"

echo "Creating backup of previously gathered logs: $BACKUP_FILE"
zip -rmq $BACKUP_FILE logs -x \*.zip

echo -e "Gathering logs from agent machines with user: $AGENT_USER\n"

# iterate over unique hosts in settings/scenario.conf
cut -d"|" -f1 settings/scenario.conf |sort |uniq |while read host
do
  echo "Gathering logs from" $host

  # create local temp directory for each host
  mkdir -p logs/$host/tmp

  # create a zip package with all the logs on remote agent
  ssh -n $AGENT_USER@$host eval "'cd $AGENT_DIR/testcases; zip -rq logs.zip . -i \*log\*'"

  # download the newly created zip from agent to local temp directory
  scp -q $AGENT_USER@$host:$AGENT_DIR/testcases/logs.zip logs/$host/tmp

  # delete the zip package on remote agent
  ssh -n $AGENT_USER@$host eval "'rm $AGENT_DIR/testcases/logs.zip'"

  # extract the zip package in local temp directory
  unzip -q logs/$host/tmp/logs.zip -d logs/$host/tmp

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
      done
      cd ../..
    fi
  done

  # finally we can delete the local temp directory
  cd ../../..
  rm -r logs/$host/tmp
done
echo "Done."

exit 0
