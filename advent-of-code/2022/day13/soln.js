import fs from "fs"

let valid = false
function validate(left, right, depth = 0) {
    while (left.length > 0 || right.length > 0) {
        let l = left.shift()
        let r = right.shift()
        if (l === undefined) {
            // console.log(' '.repeat(depth) + `- Left side ran out of items, so inputs are in the right order`)
            valid = true
            throw new Error('Valid packet')
        }
        if (r === undefined) {
            // console.log(' '.repeat(depth) + `- Right side ran out of items, so inputs are not in the right order`)
            throw new Error('Invalid packet')
        }
        // console.log(' '.repeat(depth + 1) + `- Compare ${l} vs ${r}`)
        if (typeof l == 'object' && typeof r != 'object') {
            r = [r]
        }
        if (typeof r == 'object' && typeof l != 'object') {
            l = [l]
        }
        if (typeof l == 'object' && typeof r == 'object') {
            validate(l, r, depth + 2)
        } else {
            l = parseInt(l, 10)
            r = parseInt(r, 10)
            if (r > l) {
                // console.log(' '.repeat(depth + 2) + '- Left side is smaller, so inputs are in the right order')
                valid = true
                throw new Error('Valid packet')
            } else if (r == l) {
                continue
            } else {
                // console.log(' '.repeat(depth + 2) + '- Right side is smaller, so inputs are not in the right order')
                throw new Error('Invalid packet')
            }
        }
    }
}

export function soln(inp) {
    let pair = 1
    let result = []
    for (const item of inp.split("\n\n")) {
        // console.log(`== Pair ${pair} == `)
        let [left, right] = item.split("\n")
        left = eval(left)
        right = eval(right)
        try {
            valid = false
            validate(left, right)
        } catch (error) {
        }
        if (valid) {
            result.push(pair)
        }
        pair += 1
    }
    let ans = result.reduce((acc, i) => { return acc + i })
    // console.log(ans)
    return ans
}

export function soln2(inp) {
    let valid = false
    function validate(left, right, depth = 0) {
        while (left.length > 0 || right.length > 0) {
            let l = left.shift()
            let r = right.shift()
            if (l === undefined) {
                // console.log(' '.repeat(depth) + `- Left side ran out of items, so inputs are in the right order`)
                valid = true
                throw new Error('Valid packet')
            }
            if (r === undefined) {
                // console.log(' '.repeat(depth) + `- Right side ran out of items, so inputs are not in the right order`)
                throw new Error('Invalid packet')
            }
            // console.log(' '.repeat(depth + 1) + `- Compare ${l} vs ${r}`)
            if (typeof l == 'object' && typeof r != 'object') {
                r = [r]
            }
            if (typeof r == 'object' && typeof l != 'object') {
                l = [l]
            }
            if (typeof l == 'object' && typeof r == 'object') {
                validate(l, r, depth + 2)
            } else {
                l = parseInt(l, 10)
                r = parseInt(r, 10)
                if (r > l) {
                    // console.log(' '.repeat(depth + 2) + '- Left side is smaller, so inputs are in the right order')
                    valid = true
                    throw new Error('Valid packet')
                } else if (r == l) {
                    continue
                } else {
                    // console.log(' '.repeat(depth + 2) + '- Right side is smaller, so inputs are not in the right order')
                    throw new Error('Invalid packet')
                }
            }
        }
    }
    let first = [[2]]
    let second = [[6]]
    let items = []
    for (let item of inp.split("\n")) {
        if (item.trim().length == 0) {
            continue
        }
        items.push(eval(item))
    }
    items.push(first)
    items.push(second)
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
    function compare(a, b) {
        a = deepCopy(a)
        b = deepCopy(b)
        let gt = false
        let lt = false
        valid = false
        try {
            validate(a, b)
        } catch (error) { }
        if (valid) {
            gt = 1
        }
        valid = false
        try {
            validate(b, a)
        } catch (error) { }
        if (valid) {
            lt = 1
        }
        if (gt) {
            return -1
        }
        if (lt) {
            return 1
        }
        return 0
    }
    items.sort(compare)
    // console.log(items)
    let a = 0
    let b = 0
    for (let [i, item] of Object.entries(items)) {
        if (item.length != 1 || item[0].length != 1) {
            continue
        }
        item = item && item[0] && item[0][0]
        if (item === 2) {
            a = i
        } else if (item === 6) {
            b = i
        }
    }
    a = parseInt(a, 10) + 1
    b = parseInt(b, 10) + 1
    // console.log(a, b)
    // console.log(a * b)
    return a * b
}

export const eg = `[1, 1, 3, 1, 1]
[1, 1, 5, 1, 1]

[[1], [2, 3, 4]]
[[1], 4]

[9]
[[8, 7, 6]]

[[4, 4], 4, 4]
[[4, 4], 4, 4, 4]

[7, 7, 7, 7]
[7, 7, 7]

[]
[3]

[[[]]]
[[]]

[1, [2, [3, [4, [5, 6, 7]]]], 8, 9]
[1, [2, [3, [4, [5, 6, 0]]]], 8, 9]`
console.log(soln(eg))
console.log(soln(fs.readFileSync("input.txt").toString().trim()))
console.log(soln2(eg))
console.log(soln2(fs.readFileSync("input.txt").toString().trim()))