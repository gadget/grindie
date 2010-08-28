from java.util import Date
from java.util.regex import Pattern
from java.text import SimpleDateFormat
from net.grinder.script.Grinder import grinder

# returns the current date string in the given format
def currentDate(format = 'yyyy.MM.dd'):
  df = SimpleDateFormat(format)
  return df.format(Date())

# TODO
def getValueByRegEx(response, pattern):
  p = Pattern.compile(pattern)
  matcher = p.matcher(response.getText())
  if matcher.find():
    return matcher.group()
  else:
    return ''

# write the response out to disk
def logResponse(response):
  fileName = grinder.getFilenameFactory().createFilename('responselog', '_%d.html' % grinder.runNumber)
  f = open(fileName, 'w')
  f.write(response.getText())
  f.close()
