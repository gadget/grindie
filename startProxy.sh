#!/bin/sh

. ./settings/envProps.sh

OUT_FILE=${1:-grinder.py}

$JAVA_HOME/bin/java -cp $CLASSPATH net.grinder.TCPProxy -console -http  $GRINDER_HOME/etc/httpToJythonScript.xsl > $OUT_FILE
