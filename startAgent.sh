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

usage() {
  echo -e "Usage: $0 [options] [arguments]\n\nOptions:"
  echo "  -a agent name"
  echo "  -c testcase (required)"
  echo "  -p number of processes"
  echo "  -t number of threads"
}

AGENT_NAME="singleagent"
TESTCASE=
PROCESSES=1
THREADS=1

E_INVALID_OPTION=101
while getopts "ha:c:p:t" OPTION
do
  case $OPTION in
    h) usage; exit 0;;
    a) AGENT_NAME=$OPTARG;;
    c) TESTCASE=$OPTARG;;
    p) PROCESSES=$OPTARG;;
    t) THREADS=$OPTARG;;
    ?) usage; exit $E_INVALID_OPTION;;
  esac
done
shift $((OPTIND - 1))

export TESTCASE_PARAM1=${1:-none}
export TESTCASE_PARAM2=${2:-none}

BASE_DIR="`pwd`"

E_NO_TESTCASE_SPECIFIED=102
if [ -z $TESTCASE ]
then
  usage
  exit $E_NO_TESTCASE_SPECIFIED
fi

E_GRINDER_NOT_FOUND=103
if [ ! -d $GRINDER_HOME ]
then
  echo "Grinder cannot be found!"
  echo "-get Grinder from http://grinder.sourceforge.net"
  echo -e "-set the GRINDER_HOME variable properly\n"
  exit $E_GRINDER_NOT_FOUND
fi

E_TESTCASE_NOT_FOUND=104
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
-Dgrinder.hostID="$AGENT_NAME" -cp $GRINDER_HOME/lib/grinder.jar net.grinder.Grinder grinder.properties
check_ret

cd $BASE_DIR

exit 0
