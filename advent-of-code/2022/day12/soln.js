import fs from "fs"
const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
const ALPHABET = {}
for (let i = 0; i < alphabet.length; i++) {
    const element = alphabet[i];
    ALPHABET[element] = i
}

function soln(inp) {
    let grid = []
    let s_x;
    let s_y;
    let e_x;
    let e_y;
    for (const row of inp.split("\n")) {
        if (row.indexOf('S') !== -1) {
            s_x = row.indexOf('S')
            s_y = grid.length
        }
        if (row.indexOf('E') !== -1) {
            e_x = row.indexOf('E')
            e_y = grid.length
        }
        grid.push(row)
    }
    const dirs = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
    ]
    // console.log(grid)
    // console.log(s_x, s_y)
    // console.log(e_x, e_y)
    let queue = [
        [s_x, s_y, 0, new Set()]
    ]
    let dists = []
    while (queue.length > 0) {
        let [i_x, i_y, depth, visited] = queue.shift()
        // console.log(`Processing ${i_x},${i_y}`)
        if (i_x == e_x && i_y == e_y) {
            dists.push(depth)
            continue
        }
        // console.log(grid)
        let curr = grid[i_y][i_x]
        if (curr === "S") {
            curr = 'a'
        }
        for (const [d_x, d_y] of dirs) {
            let [n_x, n_y] = [i_x + d_x, i_y + d_y]
            if (grid[n_y] !== undefined && grid[n_y][n_x] !== undefined) {
                let next = grid[n_y][n_x]
                if (next === 'E') {
                    next = 'z'
                }
                if (ALPHABET[next] - ALPHABET[curr] <= 1) {
                    // console.log(`Can move from ${grid[i_y][i_x]} to ${grid[n_y][n_x]} `)
                    if (!visited.has(`${n_x},${n_y}`)) {
                        visited.add(`${n_x},${n_y}`)
                        // console.log(`Adding ${n_x},${n_y} to queue`)
                        queue.push([n_x, n_y, depth + 1, visited])
                    }
                }
            }
        }
    }
    console.log(Math.min(dists))
}

function soln2(inp) {
    let grid = []
    let starts = []
    let e_x;
    let e_y;
    inp = inp.split("\n")
    for (let y = 0; y < inp.length; y++) {
        const newRow = []
        for (let x = 0; x < inp[y].length; x++) {
            const element = inp[y][x];
            switch (element) {
                case 'S':
                    newRow.push('a')
                    starts.push([x, y])
                    break;
                case 'E':
                    newRow.push('z')
                    e_x = x
                    e_y = y
                    break;
                case 'a':
                    newRow.push('a')
                    starts.push([x, y])
                    break;

                default:
                    newRow.push(element)
                    break;
            }
        }
        grid.push(newRow)
    }
    const dirs = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
    ]
    let min = Number.MAX_VALUE
    for (const [s_x, s_y] of starts) {
        let queue = [
            [s_x, s_y, 0, new Set()]
        ]
        while (queue.length > 0) {
            let [i_x, i_y, depth, visited] = queue.shift()
            if (i_x == e_x && i_y == e_y) {
                min = Math.min(min, depth)
                continue
            }
            if (depth > min) {
                continue
            }
            let curr = grid[i_y][i_x]
            for (const [d_x, d_y] of dirs) {
                let [n_x, n_y] = [i_x + d_x, i_y + d_y]
                if (grid[n_y] !== undefined && grid[n_y][n_x] !== undefined) {
                    let next = grid[n_y][n_x]
                    if (ALPHABET[next] - ALPHABET[curr] <= 1) {
                        if (!visited.has(`${n_x},${n_y}`)) {
                            visited.add(`${n_x},${n_y}`)
                            queue.push([n_x, n_y, depth + 1, visited])
                        }
                    }
                }
            }
        }
    }
    console.log(min)
}

const eg = `Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())