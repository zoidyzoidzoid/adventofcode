import os
import parseutils
import sets
import streams


var diff = 0
var line = ""
var score = 0
var values = initSet[int]()

proc soln(): int =
  while true:
    var fs = newFileStream(paramStr(1), fmRead)
    if not isNil(fs):
      while fs.readLine(line):
        discard parseInt(line, diff)
        score += diff
        if values.contains(score):
          return score
        values.incl(score)
      fs.close()

echo soln()
