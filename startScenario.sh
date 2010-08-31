#!/bin/sh

. ./settings/agentProps.sh

echo -e "Starting all agents with user: $AGENT_USER\n"

idx=0
while read line
do
  idx=`expr $idx + 1`
  agent_name="agent-$idx"
  host=`echo $line |cut -d"|" -f1`
  params=`echo $line |cut -d"|" -f2`
  echo "Starting $agent_name: $host ($params)"
  nohup ssh -n $AGENT_USER@$host eval "'cd $AGENT_DIR; ./startAgent.sh $agent_name $params &'" &
done < settings/scenario.conf
echo "Done."
