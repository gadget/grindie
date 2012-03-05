#!/bin/sh

#
# global variables used by grindie scripts
#

# host and port of the grinder console
export CONSOLE_HOST="your.ip"
export CONSOLE_PORT="6372"

# authentication details for the agent machines
export AGENT_USER="ec2-user"
export AGENT_KEY="$HOME/.ssh/id_rsa"
# remote base directory for the grindie package
export AGENT_DIR="/home/ec2-user/loadtest"

