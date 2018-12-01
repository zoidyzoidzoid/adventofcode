import os
import parseutils
import streams


var diff = 0
var fs = newFileStream(paramStr(1), fmRead)
var line = ""
var score = 0

if not isNil(fs):
  while fs.readLine(line):
    discard parseInt(line, diff)
    score += diff
  fs.close()

echo score

