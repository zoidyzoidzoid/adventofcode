const fs = require('fs');

const eg = `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())
function soln(inp) {
  let max = 0
  for (const elf of inp.split("\n\n")) {
    let total = 0
    for (const item of elf.split("\n")) {
      total += parseInt(item, 10)
    }
    max = Math.max(max, total)
  }
  console.log(max)
}

function soln2(inp) {
  let totals = []
  for (const elf of inp.split("\n\n")) {
    let total = 0
    for (const item of elf.split("\n")) {
      total += parseInt(item, 10)
    }
    totals.push(total)
  }
  function compareNumbers(a, b) {
    // I probably am gonna need a stdlib for JS
    if (a === Infinity || a === NaN || b === Infinity || b === NaN) {
      throw new Error(`Unsupported type in input: ${a} ${b}`)
    }
    return a - b;
  }
  totals.sort(compareNumbers)
  console.log(totals[totals.length-1] + totals[totals.length-2] + totals[totals.length-3])
}
