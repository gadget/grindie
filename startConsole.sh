#!/bin/sh

. ./settings/envProps.sh

$JAVA_HOME/bin/java -Xms32M -Xmx256M -cp $CLASSPATH net.grinder.Console
