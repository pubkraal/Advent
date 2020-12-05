package main

import (
	"fmt"
	"log"

	"github.com/pubkraal/Advent/2020/util"
)

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	chart := buildChart(lines)
	fmt.Println("Step 1:", numTreesForSlope(chart, 3, 1))

	slopes := [][]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	product := 1
	for _, slope := range slopes {
		product *= numTreesForSlope(chart, slope[0], slope[1])
	}

	fmt.Println("Step 2:", product)

}

func buildChart(lines []string) [][]int {
	chart := make([][]int, len(lines))
	for row, line := range lines {
		long := make([]int, len(line))
		for idx, char := range line {
			tree := 0
			if char == '#' {
				tree = 1
			}
			long[idx] = tree
		}
		chart[row] = long
	}

	return chart
}

func numTreesForSlope(chart [][]int, x, y int) int {
	trees := chart[0][0]
	width := len(chart[0])
	for i := 0; i < (len(chart)-1)/y; i++ {
		posx := (i + 1) * x
		posy := (i + 1) * y
		trees += chart[posy][posx%width]
	}
	return trees
}
