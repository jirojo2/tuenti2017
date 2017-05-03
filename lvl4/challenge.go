package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
	"strings"
)

func intrange(n int) []int {
	r := make([]int, n)
	for i := 0; i < n; i++ {
		r[i] = i
	}
	return r
}

// returns the k-combinations of the input iterable
func combinations(iterable []int, r int, abort chan bool) <-chan []int {
	c := make(chan []int)

	go func() {
		defer close(c)

		n := len(iterable)
		if r > n {
			return
		}
		indices := intrange(r)

		x := make([]int, r)
		for k, i := range indices {
			x[k] = iterable[i]
		}
		c <- x

		for {
			select {
			case <-abort:
				return
			default:
			}

			i := r - 1
			exit := true
			for ; i >= 0; i-- {
				if indices[i] != i+n-r {
					exit = false
					break
				}
			}
			if exit {
				return
			}
			indices[i]++
			for j := i + 1; j < r; j++ {
				indices[j] = indices[j-1] + 1
			}

			x := make([]int, r)
			for k, i := range indices {
				x[k] = iterable[i]
			}

			c <- x
		}
	}()
	return c
}

func validTriangle(a, b, c int) bool {
	return a+b > c && a+c > b && b+c > a
}

func filter(v []int, m int) []int {
	if m <= 0 {
		return v
	}
	filtered := make([]int, 0)
	for _, x := range v {
		if m >= x {
			filtered = append(filtered, x)
		}
	}
	return filtered
}

func minTriangle(lengths []int) int {
	// sort the input vector, so we prioritize the smaller edges.
	sort.Ints(lengths)

	candidate := 0
	filtered := filter(lengths, 0)
	for {
		found := 0
		abort := make(chan bool)
		if len(filtered) == 0 {
			break
		}
		ch := combinations(filtered, 3, abort)
		for v := range ch {
			if validTriangle(v[0], v[1], v[2]) {

				// calculate the triangle perimeter
				perim := v[0] + v[1] + v[2]

				// and get the biggest edge
				max := v[0]
				for _, x := range v {
					if x > max {
						max = x
					}
				}

				// if we find a valid candidate
				if candidate == 0 || perim < candidate {
					candidate = perim

					// remove the edges bigger than the biggest edge
					// this reduces a lot the complexity of the problem
					filtered = filter(lengths, max)
					found++
					break
				}
			}
			if found > 0 {
				abort <- true
				break
			}
		}
		if found == 0 {
			break
		}
	}
	return candidate
}

func main() {
	filePath := "testInput.txt"
	if len(os.Args) > 1 {
		filePath = os.Args[1]
	}

	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(data), "\n")
	n, err := strconv.Atoi(lines[0])
	if err != nil {
		panic(err)
	}

	for i := 0; i < n; i++ {
		line := lines[i+1]
		tokens := strings.Split(line, " ")
		lengths := make([]int, len(tokens)-1)
		for j := 0; j < len(tokens)-1; j++ {
			lengths[j], err = strconv.Atoi(tokens[j+1])
			if err != nil {
				panic(err)
			}
		}
		triangle := minTriangle(lengths)
		solution := "IMPOSSIBLE"
		if triangle > 0 {
			solution = strconv.Itoa(triangle)
		}
		fmt.Printf("Case #%d: %s\n", i+1, solution)
	}
}
