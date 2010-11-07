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

# iterate over unique hosts in settings/scenario.conf
cut -d"|" -f1 settings/scenario.conf |sort |uniq |while read host
do
  echo "Distributing package to" $host

  # create directory for the agent on remote machine (if not exists)
  SSH_COMMAND="ssh -n $AGENT_USER@$host 'mkdir -p $AGENT_DIR'"
  eval $SSH_COMMAND

  # synchronize the content of local (source) and remote (destination) directory
  RSYNC_COMMAND="rsync -r --exclude='*log*' $RSYNC_KEEPENV * $AGENT_USER@$host:$AGENT_DIR"
  eval $RSYNC_COMMAND
done
echo "Done."

exit 0
