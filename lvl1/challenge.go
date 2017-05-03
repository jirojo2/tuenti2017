package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	data, err := ioutil.ReadFile(os.Args[1])
	check(err)

	lines := strings.Split(string(data), "\n")
	n, err := strconv.Atoi(lines[0])
	check(err)

	var orders []int
	for i := 0; i < n; i++ {
		slices := strings.Split(lines[i*2+2], " ")

		totalSlices := 0
		for _, s := range slices {
			v, err := strconv.Atoi(s)
			check(err)
			totalSlices += v
		}

		pizzas := totalSlices / 8
		if totalSlices%8 != 0 {
			pizzas++
		}
		orders = append(orders, pizzas)
	}

	for i, order := range orders {
		fmt.Printf("Case #%d: %d\n", i+1, order)
	}
}
