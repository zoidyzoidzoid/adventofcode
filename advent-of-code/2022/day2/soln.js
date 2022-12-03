const fs = require('fs');

const one = {"A": "R", "B": "P", "C": "S"}
const two = {"X": "R", "Y": "P", "Z": "S"}
const score = {"R": 1, "P": 2, "S": 3}

eg = `A Y
B X
C Z`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())
function soln(inp) {
  // console.log(inp)
  let total1 = 0
  let total2 = 0
  for (const item of inp.split("\n")) {
    let [x, y] = item.split(" ")
    // console.log(x, y)
    x = one[x]
    y = two[y]
    total1 = total1 + score[x]
    total2 = total2 + score[y]
    if (x == y) {
      total1 = total1 + 3
      total2 = total2 + 3
    } else if ((y == "R" && x == "S") || (y == "S" && x == "P") || (y == "P" && x == "R")) {
        total1 = total1 + 0
        total2 = total2 + 6
    } else {
        total1 = total1 + 6
        total2 = total2 + 0
    }
  }
  console.log(total1)
  console.log(total2)
}

function soln2(inp) {
  // console.log(inp)
  let total1 = 0
  let total2 = 0
  for (const item of inp.split("\n")) {
    let [x, y] = item.split(" ")
    // console.log(x, y)
    x = one[x]
    y = {
      "P": { "X": "R",
      "Y": "P",
      "Z": "S",
      },
      "R": {"X": "S",
      "Y": "R",
      "Z": "P",
    },
      "S": { "X": "P",
      "Y": "S",
      "Z": "R",
      },
    }[x][y]
    total1 = total1 + score[x]
    total2 = total2 + score[y]
    if (x == y) {
      total1 = total1 + 3
      total2 = total2 + 3
    } else if ((y == "R" && x == "S") || (y == "S" && x == "P") || (y == "P" && x == "R")) {
        total1 = total1 + 0
        total2 = total2 + 6
    } else {
        total1 = total1 + 6
        total2 = total2 + 0
    }
  }
  console.log(total1)
  console.log(total2)
}
