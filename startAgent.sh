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

. ./settings/envProps.sh
. ./settings/agentProps.sh

#
# e.g. ./startAgent.sh agent-0 sample 1 4 Chuck Norris
# AGENT_NAME=agent-0
# TESTCASE=sample
# PROCESSES=1
# THREADS=4
# TESTCASE_PARAM1=Chuck
# TESTCASE_PARAM2=Norris
#

AGENT_NAME=$1
TESTCASE=$2
PROCESSES=${3:-1}
THREADS=${4:-1}
export TESTCASE_PARAM1=${5:-none}
export TESTCASE_PARAM2=${6:-none}

BASE_DIR="`pwd`"

E_USAGE=101
if [ -z $TESTCASE ] || [ "$TESTCASE" = "-h" ] || [ "$TESTCASE" = "--help" ]
then
  echo -e "Usage: ./startAgent.sh [agent_name [testcase [processes [threads [testcase_params]]]]]\n"
  exit $E_USAGE
fi

E_GRINDER_NOT_FOUND=102
if [ ! -d $GRINDER_HOME ]
then
  echo "Grinder cannot be found!"
  echo "-get Grinder from http://grinder.sourceforge.net"
  echo -e "-set the GRINDER_HOME variable properly in settings/envProps.sh\n"
  exit $E_GRINDER_NOT_FOUND
fi

E_TESTCASE_NOT_FOUND=103
if [ ! -d testcases/$TESTCASE ]
then
  echo -e "Testcase $TESTCASE cannot be found!\n"
  exit $E_TESTCASE_NOT_FOUND
fi

echo "Running testcase: $TESTCASE (processes=$PROCESSES / threads=$THREADS)"
echo "Agent: $AGENT_NAME"
echo "Testcase params: [$TESTCASE_PARAM1, $TESTCASE_PARAM2]"

cd testcases/$TESTCASE
$JAVA_HOME/bin/java -Dgrinder.processes="$PROCESSES" -Dgrinder.threads="$THREADS" \
-Dgrinder.consoleHost="$CONSOLE_HOST" -Dgrinder.consolePort="$CONSOLE_PORT" \
-Dgrinder.jvm="$JAVA_HOME/bin/java" -Dgrinder.logDirectory="log" \
-Dgrinder.hostID="$AGENT_NAME" -cp $CLASSPATH net.grinder.Grinder grinder.properties

cd $BASE_DIR

exit 0
