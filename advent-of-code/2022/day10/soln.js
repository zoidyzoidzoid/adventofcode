import fs from "fs"

function soln(inp) {
    inp = inp.split("\n")
    let result = 0
    // Registers and their state
    let state = {
        "x": 1
    }
    // Map of cycle and operations that'll happen during that
    let queue = {}
    let cycle = 0;
    let pointer = -1;
    let activeOp = false;
    while (cycle <= 220) {
        if ((cycle + 20) % 40 === 0) {
            console.log(`Cycle ${cycle}: ${cycle} * ${state['x']}`)
            result += cycle * state['x']
            // console.log(result)
            // console.log(queue)
            // console.log(state)
            // console.log()
        }
        if (cycle == 220) {
            break
        }
        if (activeOp) {
            activeOp = false
        } else {
            pointer = (pointer + 1) % inp.length
            const item = inp[pointer]
            if (item !== "noop") {
                let [op, val] = item.split(" ")
                if (op !== "addx") {
                    throw new Error("Unexpected operation")
                }
                val = parseInt(val, 10)
                queue[cycle + 2] = queue[cycle + 2] || {}
                queue[cycle + 2]["x"] = queue[cycle + 2]["x"] || 0
                queue[cycle + 2]["x"] += val
                activeOp = true
            }
        }
        if (queue[cycle] !== undefined) {
            for (const [reg, delta] of Object.entries(queue[cycle])) {
                // console.log(`Cycle ${cycle}: Updating from ${state[reg]} to ${state[reg] + delta}, diff=${delta}`)
                state[reg] += delta
            }
            delete queue[cycle]
        }
        cycle += 1
    }
    console.log(result)
}

function soln2(inp) {
    inp = inp.split("\n")
    // Registers and their state
    let state = {
        "x": 1
    }
    // Map of cycle and operations that'll happen during that
    let queue = {}
    let cycle = 0;
    let pointer = -1;
    let activeOp = false;
    let row = ''
    while (cycle <= 240) {
        if (cycle == 240) {
            break
        }
        if (activeOp) {
            activeOp = false
        } else {
            pointer = (pointer + 1) % inp.length
            const item = inp[pointer]
            if (item !== "noop") {
                let [op, val] = item.split(" ")
                if (op !== "addx") {
                    throw new Error("Unexpected operation")
                }
                val = parseInt(val, 10)
                queue[cycle + 2] = queue[cycle + 2] || {}
                queue[cycle + 2]["x"] = queue[cycle + 2]["x"] || 0
                queue[cycle + 2]["x"] += val
                activeOp = true
            }
        }
        if (queue[cycle] !== undefined) {
            for (const [reg, delta] of Object.entries(queue[cycle])) {
                // console.log(`Cycle ${cycle}: Updating from ${state[reg]} to ${state[reg] + delta}, diff=${delta}`)
                state[reg] += delta
            }
            delete queue[cycle]
        }
        if (cycle > 1 && cycle % 40 === 0) {
            console.log(row, row.length)
            row = ''
        }
        const drawn_pos_x = cycle % 40
        const sprite_pos_x = state['x']
        if ([sprite_pos_x, sprite_pos_x - 1, sprite_pos_x + 1].indexOf(drawn_pos_x) !== -1) {
            row += '#'
        } else {
            row += '.'
        }
        cycle += 1
    }
    console.log(row, row.length)
}

const eg = `addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())