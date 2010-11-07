#!/bin/sh

. ./settings/envProps.sh

HEAP_MIN=32M
HEAP_MAX=256M

$JAVA_HOME/bin/java -Xms$HEAP_MIN -Xmx$HEAP_MAX -cp $CLASSPATH net.grinder.Console

exit 0
