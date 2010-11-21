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
