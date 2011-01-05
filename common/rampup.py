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

from net.grinder.script.Grinder import grinder
from java.lang import System

# the time (in msec) you want to wait before starting a testcase on the current thread
BASE_TIME = 300

# TODO: explain
AGENT_OFFSET=10000

def __getMaxThread():
  return grinder.getProperties().getInt('grinder.threads', 0)

# halt the current thread for a time based on threadNumber
def initialSleep():
  multiplier = grinder.processNumber * __getMaxThread() + grinder.threadNumber
  waitTime = BASE_TIME * multiplier
  grinder.sleep(waitTime)

# returns an incremental int value as a uniqueId for the current thread
def getId():
  agentNumber = grinder.getAgentNumber()
  if agentNumber < 0:
    agentNumber = 0

  ind = agentNumber * AGENT_OFFSET + grinder.processNumber * __getMaxThread() + grinder.threadNumber + 1
  return ind

# generate a unique userName with an incremental suffix
def generateUserName(base):
  return base + str(getId())
