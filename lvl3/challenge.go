package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func cards(x int) int {
	// After hours attempting greedy algorithms with fibonnaci representations (e.g.: Zeckendorf's theorem)
	// I realise... log2...
	// The challenge is badly explained thou.
	return int(math.Ceil(math.Log2(float64(x))))
}

func main() {
	filePath := "testInput.txt"
	if len(os.Args) > 1 {
		filePath = os.Args[1]
	}

	data, err := ioutil.ReadFile(filePath)
	check(err)

	lines := strings.Split(string(data), "\n")
	n, err := strconv.Atoi(lines[0])
	check(err)

	for i := 0; i < n; i++ {
		maxPoints, err := strconv.Atoi(lines[i+1])
		check(err)
		fmt.Printf("Case #%d: %d\n", i+1, cards(maxPoints))
	}
}
