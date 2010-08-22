#!/bin/sh

. ./settings/agentProps.sh

echo -e "Starting all agents with user: $AGENT_USER\n"

while read line
do
  host=`echo $line |cut -d"|" -f1`
  params=`echo $line |cut -d"|" -f2`
  echo "Starting agent: $host ($params)"
  nohup ssh -n $AGENT_USER@$host eval "'cd $AGENT_DIR; ./startAgent.sh $params &'" &
done < settings/agentHosts.conf
echo "Done."
