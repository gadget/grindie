#!/bin/sh

. ./settings/agentProps.sh

process_line() {
  idx=$1
  line=$2 # e.g. localhost|sample 1 2 0 Chuck Norris

  agent_name="agent-$idx"
  host=`echo $line |cut -d"|" -f1`
  params=`echo $line |cut -d"|" -f2`
  echo "Starting $agent_name: $host ($params)"
  nohup ssh -n $AGENT_USER@$host eval "'cd $AGENT_DIR; ./startAgent.sh $agent_name $params &'" &
}

echo -e "Starting all agents with user: $AGENT_USER\n"

idx=0
while read line
do
  let idx++
  process_line $idx "$line"
done < settings/scenario.conf
echo "Done."

exit 0
