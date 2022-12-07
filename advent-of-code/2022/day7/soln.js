import { traverse } from "@babel/types"
import fs from "fs"

class Dir {
    constructor(parent, path, size = 0, children = []) {
        this.parent = parent
        this.path = path
        this.size = size
        this.children = children
    }
}

class File {
    constructor(parent, path, size) {
        this.parent = parent
        this.path = path
        this.size = size
    }
}

function soln(inp) {
    inp = inp.split("\n")
    const root = new Dir(undefined, "/")
    let loc = root;
    while (inp.length > 0) {
        const item = inp.shift()
        console.log(item)
        if (item.indexOf("$ cd ") !== -1) {
            const dest = item.slice(5)
            console.log(`changing dir to ${dest}`)
            if (dest === "/") {
                loc = root
            } else if (dest === "..") {
                loc = loc.parent
            } else {
                let found = false
                let z = undefined
                for (const f of loc.children) {
                    if (f.path === dest) {
                        found = true
                        z = f
                        break
                    }
                }
                if (!found) {
                    throw new Error("Maybe haven't explored subdir yet? Could create here")
                }
                loc = z
            }
        } else {
            console.log(`listing dir`)
            const entries = [];
            while (inp.length > 0 && inp[0].indexOf("$") !== 0) {
                entries.push(inp.shift())
            }
            console.log(entries)
            for (const entry of entries) {
                const [x, y] = entry.split(" ")
                if (x === "dir") {
                    loc.children.push(new Dir(loc, y))
                } else {
                    const size = parseInt(x, 10)
                    loc.children.push(new File(loc, y, size))
                }
            }
        }
    }

    // traverse to populate sizes
    function traverseForSize(loc) {
        if (loc.size === 0) {
            console.log(`Adding size for ${loc.path}`)
            let size = 0
            for (const entry of loc.children) {
                if (entry.constructor.name == "Dir" && entry.size === 0) {
                    size += traverseForSize(entry)
                } else {
                    size += entry.size
                }
            }
            loc.size = size
        }
        return loc.size
    }
    traverseForSize(root)

    // traverse to draw
    function traverse(loc, depth = 0) {
        console.log(" ".repeat(depth) + `- ${loc.path} (dir) (size=${loc.size})`)
        for (const entry of loc.children) {
            if (entry.constructor.name == "Dir") {
                traverse(entry, depth + 2)
            } else {
                console.log(" ".repeat(depth + 2) + `- ${entry.path} (file, size=${entry.size})`)
            }
        }
    }
    traverse(root)

    let result = 0
    function traverseForResult(loc, depth = 0) {
        if (loc.size <= 100000) {
            result += loc.size
        }
        for (const entry of loc.children) {
            if (entry.constructor.name == "Dir") {
                traverseForResult(entry, depth + 2)
            }
        }
    }
    traverseForResult(root)

    console.log(result)
}

function soln2(inp) {
    inp = inp.split("\n")
    const root = new Dir(undefined, "/")
    let loc = root;
    while (inp.length > 0) {
        const item = inp.shift()
        // console.log(item)
        if (item.indexOf("$ cd ") !== -1) {
            const dest = item.slice(5)
            // console.log(`changing dir to ${dest}`)
            if (dest === "/") {
                loc = root
            } else if (dest === "..") {
                loc = loc.parent
            } else {
                let found = false
                let z = undefined
                for (const f of loc.children) {
                    if (f.path === dest) {
                        found = true
                        z = f
                        break
                    }
                }
                if (!found) {
                    throw new Error("Maybe haven't explored subdir yet? Could create here")
                }
                loc = z
            }
        } else {
            // console.log(`listing dir`)
            const entries = [];
            while (inp.length > 0 && inp[0].indexOf("$") !== 0) {
                entries.push(inp.shift())
            }
            // console.log(entries)
            for (const entry of entries) {
                const [x, y] = entry.split(" ")
                if (x === "dir") {
                    loc.children.push(new Dir(loc, y))
                } else {
                    const size = parseInt(x, 10)
                    loc.children.push(new File(loc, y, size))
                }
            }
        }
    }

    // traverse to populate sizes
    function traverseForSize(loc) {
        if (loc.size === 0) {
            // console.log(`Adding size for ${loc.path}`)
            let size = 0
            for (const entry of loc.children) {
                if (entry.constructor.name == "Dir" && entry.size === 0) {
                    size += traverseForSize(entry)
                } else {
                    size += entry.size
                }
            }
            loc.size = size
        }
        return loc.size
    }
    traverseForSize(root)

    // // traverse to draw
    // function traverse(loc, depth = 0) {
    //     console.log(" ".repeat(depth) + `- ${loc.path} (dir) (size=${loc.size})`)
    //     for (const entry of loc.children) {
    //         if (entry.constructor.name == "Dir") {
    //             traverse(entry, depth + 2)
    //         } else {
    //             console.log(" ".repeat(depth + 2) + `- ${entry.path} (file, size=${entry.size})`)
    //         }
    //     }
    // }
    // traverse(root)

    let used = root.size
    let unused = 70000000 - used
    let goal = 30000000 - unused
    console.log(`Goal: ${goal}`)
    let candidates = []
    function traverseForResult(loc, depth = 0) {
        if (loc.size >= goal) {
            candidates.push(loc)
        }
        for (const entry of loc.children) {
            if (entry.constructor.name == "Dir") {
                traverseForResult(entry, depth + 2)
            }
        }
    }
    traverseForResult(root)

    let min = 70000000
    for (const candidate of candidates) {
        if (candidate.size < min) {
            min = candidate.size
        }
    }
    console.log(min)
}

const eg = `$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k`

soln(eg)
soln(fs.readFileSync("input.txt").toString().trim())
soln2(eg)
soln2(fs.readFileSync("input.txt").toString().trim())