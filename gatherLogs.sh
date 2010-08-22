#!/bin/sh

. ./settings/agentProps.sh

DATE_SUFFIX=`date +%Y-%m-%d_%H:%M:%S`
BACKUP_FILE="logs/backup_$DATE_SUFFIX.zip"

echo "Creating backup of previously gathered logs: $BACKUP_FILE"
zip -rmq $BACKUP_FILE logs -x \*.zip

echo -e "Gathering logs from agent machines with user: $AGENT_USER\n"

cut -d"|" -f1 settings/agentHosts.conf |sort |uniq |while read host
do
  echo "Gathering logs from" $host
  mkdir -p logs/$host/tmp
  ssh -n $AGENT_USER@$host eval "'cd $AGENT_DIR/scenarios; zip -rq logs.zip . -i \*log\*'"
  scp -q $AGENT_USER@$host:$AGENT_DIR/scenarios/logs.zip logs/$host/tmp
  ssh -n $AGENT_USER@$host eval "'rm $AGENT_DIR/scenarios/logs.zip'"
  unzip -q logs/$host/tmp/logs.zip -d logs/$host/tmp
  cd logs/$host/tmp
  for scenario in *; do
    if [ -d $scenario ]
    then
      cd $scenario/log
      for logFile in *; do
        mv $logFile ../../../$logFile.$scenario
      done
      cd ../..
    fi
  done
  cd ../../..
  rm -r logs/$host/tmp
done
echo "Done."
