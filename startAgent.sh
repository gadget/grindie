#!/bin/sh

. ./settings/envProps.sh
. ./settings/agentProps.sh

if [ -z $1 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]
then
  echo Usage: ./startAgent.sh [testcase] [processes] [threads] [agent_offset] [testcase_params]
  exit 1
fi

if [ ! -d $GRINDER_HOME ]
then
  echo Grinder cannot be found!
  echo -get Grinder from http://grinder.sourceforge.net
  echo -set the GRINDER_HOME variable properly in settings/envProps.sh
  exit 1
fi

if [ ! -d testcases/$1 ]
then
  echo Testcase $1 cannot be found!
  exit 1
fi

PROCESSES=${2:-1}
THREADS=${3:-1}
export AGENT_OFFSET=${4:-0}
export TESTCASE_PARAM1=${5:-none}
export TESTCASE_PARAM2=${6:-none}

echo "Running testcase: $1 (processes=$PROCESSES / threads=$THREADS)"
echo "Agent offset: $AGENT_OFFSET"
echo "Testcase params: [$TESTCASE_PARAM1, $TESTCASE_PARAM2]"

cd testcases/$1
$JAVA_HOME/bin/java -Dgrinder.processes="$PROCESSES" -Dgrinder.threads="$THREADS" -Dgrinder.consoleHost="$CONSOLE_HOST" -Dgrinder.consolePort="$CONSOLE_PORT" -Dgrinder.jvm="$JAVA_HOME/bin/java" -cp $CLASSPATH net.grinder.Grinder grinder.properties

cd ../..
