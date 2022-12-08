import fs from "fs"

function soln(inp) {
    inp = inp.split("\n")
    let grid = {}
    for (let i = 0; i < inp.length; i++) {
        const row = inp[i];
        for (let j = 0; j < row.length; j++) {
            const cell = row[j];
            grid[[j, i]] = cell
        }
    }
    // console.log(grid)
    // let m_x = inp[0].length
    // let m_y = inp.length
    let dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]
    const m_y = inp.length
    const m_x = inp[0].length
    let result = 0
    for (let i = 0; i < inp.length; i++) {
        const row = inp[i];
        for (let j = 0; j < row.length; j++) {
            if (i === 0 || i === m_y || j === 0 || j === m_x) {
                result += 1
                continue
            }
            let visible = 4
            const start = grid[[j, i]]
            for (const [d_x, d_y] of dirs) {
                let [c_x, c_y] = [j, i]
                while (true) {
                    c_x += d_x
                    c_y += d_y
                    if (grid[[c_x, c_y]] >= start) {
                        visible -= 1
                        break
                    }
                    if (c_x === 0 || c_x === m_x || c_y === 0 || c_y === m_y) {
                        break
                    }
                }
            }
            if (visible > 0) {
                result += 1
            }
        }
    }
    console.log(result)
}

function soln2(inp) {
    inp = inp.split("\n")
    let grid = {}
    for (let i = 0; i < inp.length; i++) {
        const row = inp[i];
        for (let j = 0; j < row.length; j++) {
            const cell = row[j];
            grid[[j, i]] = cell
        }
    }
    // console.log(grid)
    // let m_x = inp[0].length
    // let m_y = inp.length
    let dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]
    const m_y = inp.length
    const m_x = inp[0].length
    let result = 0
    for (let i = 0; i < inp.length; i++) {
        const row = inp[i];
        for (let j = 0; j < row.length; j++) {
            if (i === 0 || i === m_y || j === 0 || j === m_x) {
                continue
            }
            let visible = 4
            const canSeeDirs = []
            // console.log(`Calculating for point (${j}, ${i})`)
            const start = grid[[j, i]]
            for (const [d_x, d_y] of dirs) {
                let [c_x, c_y] = [j, i]
                let canSee = 0;
                while (true) {
                    c_x += d_x
                    c_y += d_y
                    if (c_x === -1 || c_x === m_x || c_y === -1 || c_y === m_y) {
                        break
                    }
                    // console.log(`  Checking point (${c_x}, ${c_y}): ${grid[[c_x, c_y]]}`)
                    canSee += 1
                    if (grid[[c_x, c_y]] >= start) {
                        visible -= 1
                        break
                    }
                }
                canSeeDirs.push(canSee)
            }
            // if (visible === 0) {
            let score = 1
            for (const s of canSeeDirs) {
                score *= s
            }
            // console.log(j, i, canSeeDirs, score)
            result = Math.max(result, score)
            // }
        }
    }
    console.log(result)
}

const eg = `30373
25512
65332
33549
35390`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())