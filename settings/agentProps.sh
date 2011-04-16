#!/bin/sh

#
# global variables used by grindie agents themself
#

# host and port of the grinder console
export CONSOLE_HOST="your.ip"
export CONSOLE_PORT="6372"

# remote authentication details and directory for the agent machines
export AGENT_USER="ec2-user"
export AGENT_KEY="/opt/ec2-api-tools/your.privkey"
export AGENT_DIR="/home/ec2-user/loadtest"

#
# global variables that are not used by grindie but could make your life easier
# when scripting
#

# base url and context root of the target web application
export TARGET_URL="https://www.targethost.com:80"
export CONTEXT_ROOT="TargetWebApp"

# user and password pair for login to the target web application
export TEST_USERNAME="TestUser"
export TEST_PASSWORD="secret"
