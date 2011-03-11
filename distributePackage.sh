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

echo "Distributing package to agent machines with user: $AGENT_USER"

RSYNC_KEEPENV=""
if [ "$1" = "--keepenv" ]
then
  RSYNC_KEEPENV="--exclude='envProps.sh'"
  echo "Keeping environment settings (envProps.sh)"
fi

echo ""

process_host() {
  host=$1
  echo "Distributing package to $host"

  # create directory for the agent on remote machine (if not exists)
  SSH_COMMAND="ssh -n $AGENT_USER@$host 'mkdir -p $AGENT_DIR'"
  eval $SSH_COMMAND
  checkRet

  # synchronize the content of local (source) and remote (destination) directory
  RSYNC_COMMAND="rsync -r --exclude='*log*' $RSYNC_KEEPENV * $AGENT_USER@$host:$AGENT_DIR"
  eval $RSYNC_COMMAND
  checkRet
}

iterateOverHosts process_host

echo -e "Done.\n"
exit 0
