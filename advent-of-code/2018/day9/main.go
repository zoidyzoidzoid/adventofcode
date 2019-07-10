package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func main() {
	fn := os.Args[1]
	f, err := os.Open(fn) // #nosec G304
	if err != nil {
		panic(err)
	}
	contents, err := ioutil.ReadAll(f)
	if err != nil {
		panic(err)
	}
	line := string(contents)
	args := strings.Split(line, " ")
	ps, err := strconv.Atoi(args[0])
	if err != nil {
		panic(err)
	}
	ms, err := strconv.Atoi(args[6])
	if err != nil {
		panic(err)
	}
	a(ps, ms)
	// a(ps, ms*100)
}

func a(ps int, ms int) {
	fmt.Println(ps, ms)
	loc := 0
	p := 1
	cs := []int{0}
	l := 1
	scores := map[int]int{}
	for m := 1; m < ms; m++ {
		// fmt.Println(m, cs)
		if m%23 == 0 {
			loc = (loc - 7) % l
			if loc < 0 {
				loc += l
			}
			scores[p] += m
			scores[p] += cs[loc]
			l -= 1
			cs = append(cs[:loc], cs[loc+1:]...)
		} else {
			loc = ((loc + 1) % l) + 1
			l += 1
			cs = append(cs[:loc], append([]int{m}, cs[loc:]...)...)
		}
		p = (p % ps) + 1
	}
	mx := 0
	for _, score := range scores {
		if score > mx {
			mx = score
		}
	}
	fmt.Println(mx)
}
