#!/bin/sh

. ./settings/envProps.sh
. ./settings/agentProps.sh

#
# e.g. ./startAgent.sh agent-1 sample 1 4 0 Chuck Norris
# AGENT_NAME=agent-1
# TESTCASE=sample
# PROCESSES=1
# THREADS=4
# AGENT_OFFSET=0
# TESTCASE_PARAM1=Chuck
# TESTCASE_PARAM2=Norris
#

AGENT_NAME=$1
TESTCASE=$2
PROCESSES=${3:-1}
THREADS=${4:-1}
export AGENT_OFFSET=${5:-0}
export TESTCASE_PARAM1=${6:-none}
export TESTCASE_PARAM2=${7:-none}

if [ -z $TESTCASE ] || [ "$TESTCASE" = "-h" ] || [ "$TESTCASE" = "--help" ]
then
  echo Usage: ./startAgent.sh [agent_name] [testcase] [processes] [threads] [agent_offset] [testcase_params]
  exit 1
fi

if [ ! -d $GRINDER_HOME ]
then
  echo Grinder cannot be found!
  echo -get Grinder from http://grinder.sourceforge.net
  echo -set the GRINDER_HOME variable properly in settings/envProps.sh
  exit 1
fi

if [ ! -d testcases/$TESTCASE ]
then
  echo Testcase $TESTCASE cannot be found!
  exit 1
fi

echo "Running testcase: $TESTCASE (processes=$PROCESSES / threads=$THREADS)"
echo "Agent: $AGENT_NAME"
echo "Agent offset: $AGENT_OFFSET"
echo "Testcase params: [$TESTCASE_PARAM1, $TESTCASE_PARAM2]"

cd testcases/$TESTCASE
$JAVA_HOME/bin/java -Dgrinder.processes="$PROCESSES" -Dgrinder.threads="$THREADS" -Dgrinder.consoleHost="$CONSOLE_HOST" -Dgrinder.consolePort="$CONSOLE_PORT" -Dgrinder.jvm="$JAVA_HOME/bin/java" -Dgrinder.logDirectory="log" -Dgrinder.hostID="$AGENT_NAME" -cp $CLASSPATH net.grinder.Grinder grinder.properties

cd ../..
