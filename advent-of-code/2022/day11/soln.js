import fs from "fs"

class Monkey {
    constructor(number, items, op_raw, op, test, if_true, if_false, count) {
        this.number = number
        this.items = items
        this.op_raw = op_raw
        this.op = op
        this.test = test
        this.if_true = if_true
        this.if_false = if_false
        this.count = 0
    }

    toString() {
        return `Monkey ${this.number}:
  Starting items: ${this.items}
  Operation: new = ${this.op_raw}
  Test: divisible by ${this.test}
    If true: throw to monkey ${this.if_true}
    If false: throw to monkey ${this.if_false}`
    }
}

function soln(inp) {
    const monkeys = []
    for (let item of inp.split("\n\n")) {
        item = item.split("\n")
        const number = parseInt(item[0].split(" ")[1].replace(":", ""), 10)
        const items = item[1].split(": ")[1].split(", ").map(i => parseInt(i, 10))
        const op_raw = item[2].split(" = ")[1]
        const op = (old) => {
            const command = item[2].split(" = ")[1].split(" ")
            const args = []
            if (command[0] == "old") {
                args.push(old)
            } else {
                args.push(parseInt(command[0], 10))
            }
            if (command[2] == "old") {
                args.push(old)
            } else {
                args.push(parseInt(command[2], 10))
            }
            // console.log(command, args)
            switch (command[1]) {
                case "*":
                    return args[0] * args[1]
                case "+":
                    return args[0] + args[1]
                default:
                    throw new Error(`Unsupported operation: ${command[1]}`)
            }
        }
        const test = parseInt(item[3].trim().split(" ")[3], 10)
        const if_true = parseInt(item[4].trim().split(" ")[5], 10)
        const if_false = parseInt(item[5].trim().split(" ")[5], 10)
        monkeys.push(new Monkey(number, items, op_raw, op, test, if_true, if_false))
        console.log(`${monkeys[monkeys.length - 1]} `)
    }
    let round = 1
    while (true) {
        if (round > 20) {
            break
        }

        for (const monkey of monkeys) {
            // console.log(`Monkey ${monkey.number}`)
            while (monkey.items.length > 0) {
                monkey.count += 1
                let worry = monkey.items.shift()
                if (worry == NaN || worry === undefined) {
                    throw new Error(`Something is wrong worry=${worry}`)
                }
                // console.log(`  Monkey inspects an item with a worry level of ${worry}.`)
                worry = monkey.op(worry)
                // console.log(`    Worry level is updated by ${monkey.op_raw} to ${worry}.`)

                worry = Math.floor(worry / 3)
                // console.log(`    Monkey gets bored with item. Worry level is divided by 3 to ${worry}`)

                if (worry % monkey.test === 0) {
                    // console.log(`    Current worry level is divisible by ${monkey.test}.`)
                    // console.log(`    Item with worry level ${worry} is thrown to monkey ${monkey.if_true}.`)
                    monkeys[monkey.if_true].items.push(worry)
                } else {
                    // console.log(`    Current worry level is not divisible by ${monkey.test}.`)
                    // console.log(`    Item with worry level ${worry} is thrown to monkey ${monkey.if_false}.`)
                    monkeys[monkey.if_false].items.push(worry)
                }
            }
        }

        // console.log(`Round ${round}`)
        // for (const monkey of monkeys) {
        //     console.log(`Monkey ${monkey.number}: ${monkey.items}`)
        // }

        round += 1
    }
    const counts = []
    for (const monkey of monkeys) {
        console.log(`Monkey ${monkey.number} inspected items ${monkey.count} times.`)
        counts.push(monkey.count)
    }
    counts.sort((a, b) => b - a)
    console.log(counts[0] * counts[1])
}

function soln2(inp) {
    const monkeys = []
    let lcd = 1
    for (let item of inp.split("\n\n")) {
        item = item.split("\n")
        const number = parseInt(item[0].split(" ")[1].replace(":", ""), 10)
        const items = item[1].split(": ")[1].split(", ").map(i => parseInt(i, 10))
        const op_raw = item[2].split(" = ")[1]
        const op = (old) => {
            const command = item[2].split(" = ")[1].split(" ")
            const args = []
            if (command[0] == "old") {
                args.push(old)
            } else {
                args.push(parseInt(command[0], 10))
            }
            if (command[2] == "old") {
                args.push(old)
            } else {
                args.push(parseInt(command[2], 10))
            }
            // console.log(command, args)
            switch (command[1]) {
                case "*":
                    return args[0] * args[1]
                case "+":
                    return args[0] + args[1]
                default:
                    throw new Error(`Unsupported operation: ${command[1]}`)
            }
        }
        const test = parseInt(item[3].trim().split(" ")[3], 10)
        lcd *= test
        const if_true = parseInt(item[4].trim().split(" ")[5], 10)
        const if_false = parseInt(item[5].trim().split(" ")[5], 10)
        monkeys.push(new Monkey(number, items, op_raw, op, test, if_true, if_false))
        console.log(`${monkeys[monkeys.length - 1]} `)
    }
    let round = 1
    while (true) {
        if (round - 1 > 0 && (round - 1 === 1 || round - 1 === 20 || (round - 1) % 1000 === 0)) {
            console.log(`== After round ${round - 1} ==`)
            for (const monkey of monkeys) {
                console.log(`Monkey ${monkey.number} inspected items ${monkey.count} times.`)
            }
            console.log()
        }
        if (round > 10000) {
            break
        }

        for (const monkey of monkeys) {
            // console.log(`Monkey ${monkey.number}`)
            while (monkey.items.length > 0) {
                monkey.count += 1
                let worry = monkey.items.shift()
                if (worry == NaN || worry === undefined) {
                    throw new Error(`Something is wrong worry=${worry}`)
                }
                // console.log(`  Monkey inspects an item with a worry level of ${worry}.`)
                worry = monkey.op(worry)
                // console.log(`    Worry level is updated by ${monkey.op_raw} to ${worry}.`)

                // worry = Math.floor(worry / 3)
                // console.log(`    Monkey gets bored with item. Worry level is divided by 3 to ${worry}`)

                if (worry % monkey.test === 0) {
                    // console.log(`    Current worry level is divisible by ${monkey.test}.`)
                    // console.log(`    Item with worry level ${worry} is thrown to monkey ${monkey.if_true}.`)
                    monkeys[monkey.if_true].items.push(worry % lcd)
                } else {
                    // console.log(`    Current worry level is not divisible by ${monkey.test}.`)
                    // console.log(`    Item with worry level ${worry} is thrown to monkey ${monkey.if_false}.`)
                    monkeys[monkey.if_false].items.push(worry % lcd)
                }
            }
        }

        // console.log(`Round ${round}`)
        // for (const monkey of monkeys) {
        //     console.log(`Monkey ${monkey.number}: ${monkey.items}`)
        // }

        round += 1
    }
    const counts = []
    for (const monkey of monkeys) {
        console.log(`Monkey ${monkey.number} inspected items ${monkey.count} times.`)
        counts.push(monkey.count)
    }
    counts.sort((a, b) => b - a)
    console.log(counts[0] * counts[1])
}

const eg = `Monkey 0:
            Starting items: 79, 98
        Operation: new = old * 19
        Test: divisible by 23
  If true: throw to monkey 2
  If false: throw to monkey 3

Monkey 1:
Starting items: 54, 65, 75, 74
        Operation: new = old + 6
        Test: divisible by 19
  If true: throw to monkey 2
  If false: throw to monkey 0

Monkey 2:
Starting items: 79, 60, 97
        Operation: new = old * old
        Test: divisible by 13
  If true: throw to monkey 1
  If false: throw to monkey 3

Monkey 3:
Starting items: 74
        Operation: new = old + 3
        Test: divisible by 17
  If true: throw to monkey 0
  If false: throw to monkey 1`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())