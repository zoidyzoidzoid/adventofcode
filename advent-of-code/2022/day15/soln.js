import fs from "fs"

function print_grid(grid, full = false) {
    let y_l = Math.min(...Object.keys(grid)) - 1
    let y_r = Math.max(...Object.keys(grid)) + 2
    let x_l = Number.MAX_VALUE
    let x_r = Number.MIN_VALUE
    for (const row of Object.values(grid)) {
        x_l = Math.min(x_l, Math.min(...Object.keys(row)))
        x_r = Math.max(x_r, Math.max(...Object.keys(row)))
    }
    x_l = x_l - 1
    x_r = x_r + 2
    console.log()
    for (let y = y_l; y < y_r; y++) {
        let line = `${y}: `.padStart(7)
        for (let x = x_l; x < x_r; x++) {
            line += grid[y] && grid[y][x] || '.'
        }
        if (line.indexOf('|') !== -1 || line.indexOf('~') !== -1 || full) {
            console.log(line)
        }
    }
}

function soln(inp, soln_y = 10) {
    let grid = []
    let max_dist = 0;
    for (const item of inp.split("\n")) {
        let [s, b] = item.split(": closest beacon is at x=")
        s = s.slice('Sensor at x='.length)
        s = s.split(", y=").map(i => parseInt(i, 10))
        b = b.split(", y=").map(i => parseInt(i, 10))
        let [s_x, s_y] = s
        grid[s_y] = grid[s_y] || {}
        grid[s_y][s_x] = 'S'
        let [b_x, b_y] = b
        grid[b_y] = grid[b_y] || {}
        grid[b_y][b_x] = 'B'
        let dist = Math.abs(b_x - s_x) + Math.abs(b_y - s_y)
        max_dist = Math.max(max_dist, dist)

        let j = soln_y
        // for (let j = s_y - dist * 2; j < s_y + dist * 2; j++) {
        for (let i = s_x - dist * 2; i < s_x + dist * 2; i++) {
            i = Math.floor(i)
            j = Math.floor(j)
            let dist2 = Math.abs(s_x - i) + Math.abs(s_y - j)
            if (dist2 <= dist) {
                if ((grid[j] && grid[j][i] || '.') === '.') {
                    grid[j] = grid[j] || {}
                    grid[j][i] = '#'
                }
            }
        }
        // }
    }
    // print_grid(grid, true)

    // console.log(grid[soln_y])
    let result = Object.values(grid[soln_y]).filter(i => i === '#').length
    console.log(result)
    return result
}

const deepCopy = (arr) => {
    let copy = [];
    arr.forEach(elem => {
        if (Array.isArray(elem)) {
            copy.push(deepCopy(elem))
        } else {
            copy.push(elem)
        }
    })
    return copy;
}

function soln2(inp, min_x = 0, max_x = 4000000, min_y = 0, max_y = 4000000) {
    let items = []
    const og_grid = []
    for (const item of inp.split("\n")) {
        let [s, b] = item.split(": closest beacon is at x=")
        s = s.slice('Sensor at x='.length)
        s = s.split(", y=").map(i => parseInt(i, 10))
        b = b.split(", y=").map(i => parseInt(i, 10))
        let [s_x, s_y] = s
        og_grid[s_y] = og_grid[s_y] || {}
        og_grid[s_y][s_x] = 'S'
        let [b_x, b_y] = b
        og_grid[b_y] = og_grid[b_y] || {}
        og_grid[b_y][b_x] = 'B'
        items.push([s_x, s_y, b_x, b_y])
    }
    for (let soln_y = min_y; soln_y < max_y; soln_y++) {
        let grid = deepCopy(og_grid)
        for (const [s_x, s_y, b_x, b_y] of items) {
            let dist = Math.abs(b_x - s_x) + Math.abs(b_y - s_y)

            let j = soln_y
            // for (let j = s_y - dist * 2; j < s_y + dist * 2; j++) {
            for (let i = s_x - dist; i < s_x + dist; i++) {
                if (i < min_x || i > max_x) {
                    continue
                }
                i = parseInt(Math.floor(i), 10)
                j = parseInt(Math.floor(j), 10)
                let dist2 = Math.abs(s_x - i) + Math.abs(s_y - j)
                if (dist2 <= dist) {
                    if ((grid[j] && grid[j][i] || '.') === '.') {
                        grid[j] = grid[j] || {}
                        grid[j][i] = '#'
                    }
                }
            }
        }
        // print_grid(grid, true)

        // console.log(grid[soln_y])
        // let result = Object.values(grid[soln_y]).filter(i => i === '#').length
        let result = 0
        for (let [x, c] of Object.entries(grid[soln_y])) {
            if (x < min_x || x > max_x) {
                continue
            }
            if (c !== '.') {
                result += 1
            }
        }
        if (result === max_y) {
            console.log(result, max_y)
            for (let x = min_x; x <= max_x; x++) {
                if (grid[soln_y][x] === undefined) {
                    console.log(`Found ${x},${soln_y}`)
                    let res = (x * 4000000) + soln_y
                    console.log(res)
                    return res
                }
            }
        }
    }
}


const eg = `Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3`
soln(eg, 10)
soln(fs.readFileSync("input.txt").toString().trim(), 2000000)
soln2(eg, 0, 20, 0, 20)
soln2(fs.readFileSync("input.txt").toString().trim())
