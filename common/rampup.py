from net.grinder.script.Grinder import grinder
from java.lang import System

# the time (in msec) you want to wait before starting a scenario on the current thread
BASE_TIME = 300

def __getMaxThread():
  return grinder.getProperties().getInt('grinder.threads', 0)

# halt the current thread for a time based on threadNumber
def initialSleep():
  multiplier = grinder.processNumber * __getMaxThread() + grinder.threadNumber
  waitTime = BASE_TIME * multiplier
  grinder.sleep(waitTime)

# returns an incremental int value as a uniqueId for the current thread
# TODO: explain the usage of AGENT_OFFSET
def getId():
  agentOffset = System.getenv().get('AGENT_OFFSET')
  if agentOffset == '':
    agentOffset = 0

  ind = int(agentOffset) + grinder.processNumber * __getMaxThread() + grinder.threadNumber + 1
  return ind

# generate a unique userName with an incremental suffix
def generateUserName(base):
  return base + str(getId())
