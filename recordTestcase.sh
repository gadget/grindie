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

. ./common.sh

TESTCASE=$1

E_NO_TESTCASE_SPECIFIED=101
if [ -z $TESTCASE ]
then
  echo -e "Usage: $0 [testcase]\n"
  exit $E_NO_TESTCASE_SPECIFIED
fi

E_TESTCASE_EXISTS=102
if [ -d testcases/$TESTCASE ]
then
  echo -e "Testcase $TESTCASE already exists!\n"
  exit $E_TESTCASE_EXISTS
fi

mkdir -p testcases/$TESTCASE
check_ret

echo -e "grinder.runs=1
grinder.script=grinder.py
grinder.numberOfOldLogs=32
grinder.jvm.arguments=-Xms32M -Xmx128M
grinder.sleepTimeFactor=1" > testcases/$TESTCASE/grinder.properties
check_ret

$JAVA_HOME/bin/java -cp $GRINDER_HOME/lib/grinder.jar net.grinder.TCPProxy \
-console -http $GRINDER_HOME/etc/httpToJythonScript.xsl > testcases/$TESTCASE/grinder.py
check_ret

exit 0
