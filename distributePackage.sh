#!/bin/sh

. ./settings/agentProps.sh

echo "Distributing package to agent machines with user: $AGENT_USER"

RSYNC_KEEPENV=""
if [ "$1" = "--keepenv" ]
then
  RSYNC_KEEPENV="--exclude='envProps.sh'"
  echo "Keeping environment settings (envProps.sh)"
fi

echo ""

cut -d"|" -f1 settings/agentHosts.conf |sort |uniq |while read host
do
  echo "Distributing package to" $host
  SSH_COMMAND="ssh -n $AGENT_USER@$host 'mkdir -p $AGENT_DIR'"
  eval $SSH_COMMAND
  RSYNC_COMMAND="rsync -r --exclude='*log*' $RSYNC_KEEPENV * $AGENT_USER@$host:$AGENT_DIR"
  eval $RSYNC_COMMAND
done
echo "Done."
