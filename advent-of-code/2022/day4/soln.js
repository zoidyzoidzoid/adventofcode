const fs = require('fs');

const eg = `2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`
soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())
function soln(inp) {
    let total = 0
    for (const item of inp.split("\n")) {
        const [p1, p2] = item.split(",")
        let [x1, y1] = p1.split("-")
        let [x2, y2] = p2.split("-")
        x1 = parseInt(x1, 10)
        y1 = parseInt(y1, 10)
        x2 = parseInt(x2, 10)
        y2 = parseInt(y2, 10)
        // console.log(x1, y1, x2, y2)
        if ((x1 <= x2 && y1 >= y2) || (x1 >= x2 && y1 <= y2)) {
            total = total + 1
        }
    }
    console.log(total)
}

function soln2(inp) {
    let total = 0
    for (const item of inp.split("\n")) {
        const [p1, p2] = item.split(",")
        let [x1, y1] = p1.split("-")
        let [x2, y2] = p2.split("-")
        x1 = parseInt(x1, 10)
        y1 = parseInt(y1, 10)
        x2 = parseInt(x2, 10)
        y2 = parseInt(y2, 10)
        // console.log(x1, y1, x2, y2)
        let overlap = false
        for (let i = x1; i <= y1; i++) {
            for (let j = x2; j <= y2; j++) {
                if (i == j) {
                    total = total + 1
                    overlap = true
                    break
                }
            }
            if (overlap) {
                break
            }
        }
    }
    console.log(total)
}
