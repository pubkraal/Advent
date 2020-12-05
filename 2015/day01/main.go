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

	line := lines[0]
	floor := 0
	basementPos := 0
	for idx, r := range line {
		switch r {
		case '(':
			floor++
		case ')':
			floor--
		}
		if basementPos == 0 && floor < 0 {
			basementPos = idx
		}
	}

	fmt.Println("Step 1:", floor)
	fmt.Println("Step 2:", basementPos+1)
}
