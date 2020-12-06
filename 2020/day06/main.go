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

	answers := 0
	answersAll := 0
	setLines := 0

	curset := make(map[rune]int)

	for _, line := range lines {
		if line == "" {
			answers += len(curset)
			for _, v := range curset {
				if v == setLines {
					answersAll++
				}
			}

			curset = make(map[rune]int)
			setLines = 0
			continue
		}

		for _, r := range line {
			curset[r]++
		}
		setLines++
	}

	fmt.Println("Step 1:", answers)
	fmt.Println("Step 2:", answersAll)
}
