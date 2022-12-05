import fs from "fs"

const eg = `    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`
soln(eg)
soln(fs.readFileSync("input.txt").toString())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trimEnd())
function soln(inp) {
    // console.log(inp)
    let [state1, commands] = inp.split("\n\n")
    state1 = state1.split("\n")
    let n_rows = state1.length
    let n_cols = (state1[state1.length - 1].length + 1) / 4
    // console.log(n_rows)
    // console.log(n_cols)
    let state = {}
    for (let i = n_rows - 2; i >= 0; i--) {
        const row = state1[i]
        console.log(row)
        for (let j = 0; j < n_cols; j++) {
            const box = state1[i].slice(j * 4, (j + 1) * 4)
            if (!box.trim()) {
                continue
            }
            state[j + 1] = state[j + 1] || []
            state[j + 1].push(box.trim())
        }
    }
    // console.log(state)
    for (const item of commands.split("\n")) {
        if (!item.trim()) {
            continue
        }
        const chunks = item.split(" ")
        let n = parseInt(chunks[1])
        let from = parseInt(chunks[3], 10)
        let to = parseInt(chunks[5], 10)
        // console.log(`move ${n} from ${from} to ${to}`)
        const tmp = []
        for (let index = 0; index < n; index++) {
            state[to].push(state[from].pop())
        }
        // console.log(state)
    }
    let result = ''
    for (let j = 0; j < n_cols; j++) {
        result += state[j + 1].pop().replace("[", "").replace("]", "")
    }
    console.log(result)
}

function soln2(inp) {
    // console.log(inp)
    let [state1, commands] = inp.split("\n\n")
    state1 = state1.split("\n")
    let n_rows = state1.length
    let n_cols = (state1[state1.length - 1].length + 1) / 4
    // console.log(n_rows)
    // console.log(n_cols)
    let state = {}
    for (let i = n_rows - 2; i >= 0; i--) {
        const row = state1[i]
        console.log(row)
        for (let j = 0; j < n_cols; j++) {
            const box = state1[i].slice(j * 4, (j + 1) * 4)
            if (!box.trim()) {
                continue
            }
            state[j + 1] = state[j + 1] || []
            state[j + 1].push(box.trim())
        }
    }
    // console.log(state)
    for (const item of commands.split("\n")) {
        if (!item.trim()) {
            continue
        }
        const chunks = item.split(" ")
        let n = parseInt(chunks[1])
        let from = parseInt(chunks[3], 10)
        let to = parseInt(chunks[5], 10)
        // console.log(`move ${n} from ${from} to ${to}`)
        const tmp = []
        for (let index = 0; index < n; index++) {
            tmp.push(state[from].pop())
        }
        while (tmp.length !== 0) {
            state[to].push(tmp.pop())
        }
        // console.log(state)
    }
    let result = ''
    for (let j = 0; j < n_cols; j++) {
        result += state[j + 1].pop().replace("[", "").replace("]", "")
    }
    console.log(result)
}
