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

process_line() {
  idx=$1
  line=$2 # e.g. localhost sample 1 2 Chuck Norris

  agent_name="agent-$idx"
  host=`echo $line |cut -d" " -f1`
  params=`echo $line |cut -d" " -f2-`

  echo "Starting $agent_name: $host ($params)"
  ssh -n -i $AGENT_KEY $AGENT_USER@$host eval "'cd $AGENT_DIR; nohup ./startAgent.sh $agent_name $params > $agent_name.out 2> $agent_name.err &'"
  checkRet
}

echo -e "Starting all agents with user: $AGENT_USER\n"

idx=0
while read line
do
  if [ -n "$line" ] && [ "${line:0:1}" != "#" ]
  then
    process_line $idx "$line"
    let idx++
  fi
done < settings/scenario.conf

echo -e "Done.\n"
exit 0
