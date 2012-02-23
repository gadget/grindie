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

process_host() {
  host=$1
  echo "Deleting logs on $host"

  # delete all the log files on remote agent
  ssh -n -i $AGENT_KEY $AGENT_USER@$host eval "'cd $AGENT_DIR/testcases; rm -fr */log*'"
  check_ret
}

echo -e "Deleting logs on agent machines with user: $AGENT_USER\n"

iterate_over_hosts process_host

echo -e "Done.\n"
exit 0
