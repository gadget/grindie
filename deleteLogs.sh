#!/bin/sh

. ./settings/agentProps.sh

echo -e "Deleting logs on agent machines with user: $AGENT_USER\n"

# iterate over unique hosts in settings/scenario.conf
cut -d"|" -f1 settings/scenario.conf |sort |uniq |while read host
do
  echo "Deleting logs on" $host

  # delete all the log files on remote agent
  ssh -n $AGENT_USER@$host eval "'cd $AGENT_DIR/testcases; rm -fr */log*'"
done
echo "Done."

exit 0
