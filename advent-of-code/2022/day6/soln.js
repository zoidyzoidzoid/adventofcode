import fs from "fs"

const eg = `mjqjpqmgbljsphdztnvjfqwrcgsmlb`
const eg2 = `bvwbjplbgvbhsrlpgdmjqwftvncz`
const eg3 = `nppdvjthqldpwncqszvftbrmjlhg`
const eg4 = `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`
const eg5 = `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`

console.log("Part 1")
soln(eg)
soln(eg2)
soln(eg3)
soln(eg4)
soln(eg5)
soln(fs.readFileSync("input.txt").toString())
console.log("Part 2")
soln2(eg)
soln2(eg2)
soln2(eg3)
soln2(eg4)
soln2(eg5)
soln2(fs.readFileSync("input.txt").toString())
function soln(inp) {
    inp = inp.trim()
    console.log(inp)
    let result = ''
    let start = ''
    for (let i = 0; i < inp.length - 3; i++) {
        const chunk = inp.slice(i, i + 4)
        const chunkSet = new Set(chunk)
        if (chunkSet.size == 4) {
            start = i
            result = chunk
            break
        }
    }
    console.log(start + 4, result)
}

function soln2(inp) {
    inp = inp.trim()
    console.log(inp)
    let result = ''
    let start = ''
    for (let i = 0; i < inp.length - 13; i++) {
        const chunk = inp.slice(i, i + 14)
        const chunkSet = new Set(chunk)
        if (chunkSet.size == 14) {
            start = i
            result = chunk
            break
        }
    }
    console.log(start + 14, result)
}