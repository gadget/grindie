#!/bin/sh

#
# global variables used by grindie agents themself
#

# host and port of the grinder console
export CONSOLE_HOST="localhost"
export CONSOLE_PORT="6372"

# remote user and directory for the agent machines
# note: os passwords are not stored, use key based authentication for ssh sessions
export AGENT_USER="loadtest"
export AGENT_DIR="/home/loadtest/loadtest"
export AGENT_KEY="~/.ssh/id_rsa.pub"

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
