const fs = require('fs');

const one = {"A": "R", "B": "P", "C": "S"}
const two = {"X": "R", "Y": "P", "Z": "S"}
const score = {"R": 1, "P": 2, "S": 3}

const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
const eg = `JrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())
function soln(inp) {
  // console.log(inp)
  let total = 0
  for (const item of inp.split("\n")) {
    // console.log(item.length, item.length / 2)
    const mid = Math.floor(item.length / 2)
    const a = new Set(item.slice(0, mid))
    const b = new Set(item.slice(mid))
    let intersect = new Set([...a].filter(i => b.has(i)));
    for (const t of intersect) {
      if (t !== t.toLowerCase()) {
        total = total + 27 + alphabet.indexOf(t.toLowerCase())
      } else {
        total = total + 1 + alphabet.indexOf(t)
      }
    }
    // console.log(...intersect)
  }
  console.log(total)
}

function soln2(inp) {
  // console.log(inp)
  let total = 0
  inp = inp.split("\n")
  for (let i = 0; i < inp.length; i = i + 3) {
    const a = new Set(inp[i])
    const b = new Set(inp[i+1])
    const c = new Set(inp[i+2])
    let intersect1 = new Set([...a].filter(i => b.has(i)));
    let intersect2 = new Set([...intersect1].filter(i => c.has(i)));
    for (const t of intersect2) {
      if (t !== t.toLowerCase()) {
        total = total + 27 + alphabet.indexOf(t.toLowerCase())
      } else {
        total = total + 1 + alphabet.indexOf(t)
      }
    }
    // console.log(...intersect)
  }
  console.log(total)
}
