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

#
# represents the reserved uniqueIds for each agents
# make sure that this value is big enough to provide correct uniqueness in your scenario
# e.g.
# agent-1 is running with 4 processes and 16 threads in each process (64 threads)
# agent-2 is running with 1 process and 128 threads (128 threads)
# agent-3 is running with 2 processes and 32 threads in each process (64 threads)
# in this case you need to set it at least to 128 since agent-2 will need 128 uniqueId
# that are not used by other agents
#
# default value is 10000 (should be enough for most cases)
#
AGENT_OFFSET=10000

# returns the number of threads specified for the current process
def __maxThread():
  return grinder.getProperties().getInt('grinder.threads', 0)

# halt the current thread for a time based on threadNumber
def initialSleep():
  multiplier = grinder.processNumber * __maxThread() + grinder.threadNumber
  waitTime = BASE_TIME * multiplier
  grinder.sleep(waitTime)

# returns an incremental int value as a uniqueId for the current thread
def threadId():
  agentNumber = grinder.getAgentNumber()
  # if running with no console
  if agentNumber < 0:
    agentNumber = 0

  ind = agentNumber * AGENT_OFFSET + grinder.processNumber * __maxThread() + grinder.threadNumber + 1
  return ind

# generate a unique userName with an incremental suffix
def generateUserName(base):
  return base + str(threadId())
