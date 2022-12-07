// To do this in JS, I'm probably gonna want some functions that exist in the stdlib or I can quickly implement in Python

export function compareNumbers(a, b) {
    // I probably am gonna need a stdlib for JS
    if (a === Infinity || a === NaN || b === Infinity || b === NaN) {
        throw new Error(`Unsupported type in input: ${a} ${b}`)
    }
    return a - b;
}

export function sortByNumbers(arr) {
    const result = [...arr]
    result.sort(compareNumbers)
    return result
}

export function setIntersection(set1, set2) {
    return new Set([...set1].filter(i => set2.has(i)));
}

export function setUnion(set1, set2) {
    return new Set([...set1, ...set2]);
}

export const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
