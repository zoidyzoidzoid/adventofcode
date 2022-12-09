import fs from "fs"

function soln(inp) {
    let h_x = 0;
    let h_y = 0;
    let t_x = 0;
    let t_y = 0;
    let s_x = 0;
    let s_y = 0;
    const MOVE_DIRS = {
        'U': [0, 1],
        'D': [0, -1],
        'L': [-1, 0],
        'R': [1, 0],
    }
    const TAIL_DIRS = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [0, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
    ]
    const visited = new Set([`0,0`]);
    let min_x = 0;
    let min_y = 0;
    let max_x = 0;
    let max_y = 0;
    function drawGrid() {
        for (const item of visited) {
            let [v_x, v_y] = item.split(",")
            v_x = parseInt(v_x, 10)
            v_y = parseInt(v_y, 10)
            min_x = Math.min(min_x, v_x)
            min_y = Math.min(min_y, v_y)
            max_x = Math.max(max_x, v_x)
            max_y = Math.max(max_y, v_y)
        }
        console.log()
        for (let y = min_y - 2; y <= max_y + 1; y++) {
            let row = ''
            for (let x = min_x - 2; x <= max_x + 1; x++) {
                if (x === h_x && y === h_y) {
                    row += 'H'
                } else if (x === t_x && y === t_y) {
                    row += 'T'
                } else if (x === s_x && y === s_y) {
                    row += 'S'
                } else if (visited.has(`${x},${y}`)) {
                    row += '#'
                } else {
                    row += '.'
                }
            }
            console.log(row)
        }
        console.log()
    }
    for (const item of inp.split("\n")) {
        let [dir, n] = item.split(" ")
        n = parseInt(n, 10)
        // console.log(`${dir} ${n}`)
        const [d_x, d_y] = MOVE_DIRS[dir]
        for (let i = 0; i < n; i++) {
            // move head
            h_x += d_x
            h_y += d_y
            let dist = Math.sqrt(Math.pow(t_x - h_x, 2) + Math.pow(t_y - h_y, 2))
            let [og_x, og_y] = [t_x, t_y]
            while (Math.floor(dist) > 1) {
                // move tail
                let best_move_x = 0
                let best_move_y = 0
                let best_move_min = dist
                for (const [t_d_x, t_d_y] of TAIL_DIRS) {
                    const [x, y] = [(og_x + t_d_x), (og_y + t_d_y)]
                    let pot_dist = Math.sqrt(Math.pow(x - h_x, 2) + Math.pow(y - h_y, 2))
                    if (pot_dist < best_move_min) {
                        best_move_x = x
                        best_move_y = y
                        best_move_min = pot_dist
                    }
                }
                [t_x, t_y] = [best_move_x, best_move_y]
                visited.add(`${t_x},${t_y}`)
                dist = best_move_min
                og_x = t_x
                og_y = t_y
            }
            // drawGrid()
        }
    }
    // console.log(visited)
    console.log(visited.size)
}

function soln2(inp) {
    let h_x = 0;
    let h_y = 0;
    let positions = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]
    let s_x = 0;
    let s_y = 0;
    const MOVE_DIRS = {
        'U': [0, 1],
        'D': [0, -1],
        'L': [-1, 0],
        'R': [1, 0],
    }
    const TAIL_DIRS = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [0, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
    ]
    const visited = new Set([`0,0`]);
    let min_x = 0;
    let min_y = 0;
    let max_x = 0;
    let max_y = 0;
    function drawGrid() {
        for (const item of visited) {
            let [v_x, v_y] = item.split(",")
            v_x = parseInt(v_x, 10)
            v_y = parseInt(v_y, 10)
            min_x = Math.min(min_x, v_x)
            min_y = Math.min(min_y, v_y)
            max_x = Math.max(max_x, v_x)
            max_y = Math.max(max_y, v_y)
        }
        console.log()
        for (let y = min_y - 2; y <= max_y + 1; y++) {
            let row = ''
            for (let x = min_x - 2; x <= max_x + 1; x++) {
                if (x === h_x && y === h_y) {
                    row += 'H'
                } else {
                    let seen = false
                    for (let position = 0; position < positions.length; position++) {
                        const [e_x, e_y] = positions[position];
                        if (x === e_x && y === e_y) {
                            row += `${position + 1}`
                            seen = true
                            break
                        }
                    }
                    if (seen) {
                        continue
                    } else if (x === s_x && y === s_y) {
                        row += 'S'
                    } else if (visited.has(`${x},${y}`)) {
                        row += '#'
                    } else {
                        row += '.'
                    }
                }
            }
            console.log(row)
        }
        console.log()
    }
    for (const item of inp.split("\n")) {
        let [dir, n] = item.split(" ")
        n = parseInt(n, 10)
        // console.log(`${dir} ${n}`)
        const [d_x, d_y] = MOVE_DIRS[dir]
        for (let i = 0; i < n; i++) {
            // move head
            h_x += d_x
            h_y += d_y
            let new_positions = []
            for (let j = 0; j < positions.length; j++) {
                const [c_x, c_y] = positions[j];
                let [p_x, p_y] = [h_x, h_y]
                if (j !== 0) {
                    [p_x, p_y] = positions[j - 1]
                }
                let dist = Math.sqrt(Math.pow(c_x - p_x, 2) + Math.pow(c_y - p_y, 2))
                let [og_x, og_y] = [c_x, c_y]
                while (Math.floor(dist) > 1) {
                    // move tail
                    let best_move_x = 0
                    let best_move_y = 0
                    let best_move_min = dist
                    for (const [t_d_x, t_d_y] of TAIL_DIRS) {
                        const [x, y] = [(og_x + t_d_x), (og_y + t_d_y)]
                        let pot_dist = Math.sqrt(Math.pow(x - p_x, 2) + Math.pow(y - p_y, 2))
                        if (pot_dist < best_move_min) {
                            best_move_x = x
                            best_move_y = y
                            best_move_min = pot_dist
                        }
                    }
                    positions[j] = [best_move_x, best_move_y]
                    dist = best_move_min
                    og_x = c_x
                    og_y = c_y
                }
                visited.add(`${positions[8][0]},${positions[8][1]}`)
            }
        }
        // drawGrid()
    }
    // console.log(visited)
    console.log(visited.size)
}


const eg = `R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
const eg2 = `R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20`
soln2(eg)
soln2(eg2)
soln2(fs.readFileSync("input.txt").toString().trim())