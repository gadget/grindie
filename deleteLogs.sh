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

echo -e "Deleting logs on agent machines with user: $AGENT_USER\n"

# iterate over unique hosts in settings/scenario.conf
cat settings/scenario.conf |grep -v '#' |grep -v "^$" |cut -d"|" -f1 |sort |uniq |while read host
do
  echo "Deleting logs on $host"

  # delete all the log files on remote agent
  ssh -n $AGENT_USER@$host eval "'cd $AGENT_DIR/testcases; rm -fr */log*'"
  checkRet
done

echo -e "Done.\n"
exit 0
