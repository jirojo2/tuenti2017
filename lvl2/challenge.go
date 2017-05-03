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

func score(rolls []int) []int {
	// 2 rolls each frame
	// strike => no need for a second roll
	//        => next two roll's pins are bonus
	// spare => all remaining pins kocked on the second roll
	//       => next roll's pins are bonus
	// 10th round is special, as it creates one (spare) or two (strike) rolls, just bonus points
	frames := make([]int, 10)

	const SpecialFrame = 10 - 1

	frame := 0
	roll := 0
	totalPoints := 0
	framePoints := 0
	for i := 0; i < len(rolls); i++ {
		changeFrame := false

		if rolls[i] == 10 && roll == 0 {
			// strike
			framePoints += rolls[i+1]
			framePoints += rolls[i+2]
			changeFrame = true
		} else if rolls[i]+framePoints == 10 && roll == 1 {
			// spare
			framePoints += rolls[i+1]
			changeFrame = true
		} else if roll == 1 {
			changeFrame = true
		}

		if frame != SpecialFrame || roll < 2 {
			framePoints += rolls[i]
		}

		if changeFrame {
			totalPoints += framePoints
			frames[frame] = totalPoints
			framePoints = 0
			roll = 0
			if frame == SpecialFrame {
				break
			}
			frame++
		} else {
			roll++
		}
	}

	return frames
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
		rollsStr := strings.Split(lines[i*2+2], " ")

		var rolls []int
		for _, rollStr := range rollsStr {
			roll, err := strconv.Atoi(rollStr)
			check(err)
			rolls = append(rolls, roll)
		}

		points := score(rolls)

		var pointsStr []string
		for _, p := range points {
			pointsStr = append(pointsStr, strconv.Itoa(p))
		}

		fmt.Printf("Case #%d: %s\n", i+1, strings.Join(pointsStr, " "))
	}
}
