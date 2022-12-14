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

function soln(inp) {
    let grid = {}
    grid[0] = { 500: '+' }
    for (const line of inp.split("\n")) {
        let chunks = line.split(' -> ')
        for (let i = 0; i < chunks.length - 1; i++) {
            let [x1, y1] = chunks[i].split(',')
            let [x2, y2] = chunks[i + 1].split(',')
            // console.log(x1, y1, ' -> ', x2, y2)
            x1 = parseInt(x1, 10)
            y1 = parseInt(y1, 10)
            x2 = parseInt(x2, 10)
            y2 = parseInt(y2, 10)
            if (x1 > x2) {
                [x1, x2] = [x2, x1]
            }
            if (y1 > y2) {
                [y1, y2] = [y2, y1]
            }
            for (let y = y1; y < y2 + 1; y++) {
                for (let x = x1; x < x2 + 1; x++) {
                    grid[y] = grid[y] || {}
                    grid[y][x] = '#'
                }
            }
        }
    }
    // print_grid(grid, true)

    let result = 0
    let done = false
    while (true) {
        let [c_x, c_y] = [500, 0]
        while (true) {
            if (c_y >= 10_000) {
                done = true
                break
            }
            if ((grid[c_y + 1] && grid[c_y + 1][c_x] || '.') === '.') {
                c_y += 1
            } else if ((grid[c_y + 1] && grid[c_y + 1][c_x - 1] || '.') === '.') {
                c_x -= 1
                c_y += 1
            } else if ((grid[c_y + 1] && grid[c_y + 1][c_x + 1] || '.') === '.') {
                c_x += 1
                c_y += 1
            } else {
                grid[c_y] = grid[c_y] || {}
                grid[c_y][c_x] = 'o'
                result += 1
                break
            }
        }
        if (done) {
            break
        }
    }
    // print_grid(grid, true)
    console.log(result)
}

function soln2(inp) {
    let grid = {}
    grid[0] = { 500: '+' }
    for (const line of inp.split("\n")) {
        let chunks = line.split(' -> ')
        for (let i = 0; i < chunks.length - 1; i++) {
            let [x1, y1] = chunks[i].split(',')
            let [x2, y2] = chunks[i + 1].split(',')
            // console.log(x1, y1, ' -> ', x2, y2)
            x1 = parseInt(x1, 10)
            y1 = parseInt(y1, 10)
            x2 = parseInt(x2, 10)
            y2 = parseInt(y2, 10)
            if (x1 > x2) {
                [x1, x2] = [x2, x1]
            }
            if (y1 > y2) {
                [y1, y2] = [y2, y1]
            }
            for (let y = y1; y < y2 + 1; y++) {
                for (let x = x1; x < x2 + 1; x++) {
                    grid[y] = grid[y] || {}
                    grid[y][x] = '#'
                }
            }
        }
    }
    let floor = Math.max(...Object.keys(grid)) + 2
    // console.log(`Floor at ${floor}`)
    // print_grid(grid, true)

    let result = 0
    let done = false
    while (true) {
        let [c_x, c_y] = [500, 0]
        while (true) {
            if (grid[0][500] === 'o') {
                done = true
                break
            }
            let below = grid[c_y + 1] && grid[c_y + 1][c_x] || '.'
            let diag_left = grid[c_y + 1] && grid[c_y + 1][c_x - 1] || '.'
            let diag_right = grid[c_y + 1] && grid[c_y + 1][c_x + 1] || '.'
            if (c_y + 1 === floor) {
                below = '#'
                diag_left = '#'
                diag_right = '#'
            }
            if (below === '.') {
                c_y += 1
            } else if (diag_left === '.') {
                c_x -= 1
                c_y += 1
            } else if (diag_right === '.') {
                c_x += 1
                c_y += 1
            } else {
                grid[c_y] = grid[c_y] || {}
                grid[c_y][c_x] = 'o'
                result += 1
                break
            }
        }
        if (done) {
            break
        }
    }
    // print_grid(grid, true)
    console.log(result)
}


const eg = `498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())