package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/pubkraal/Advent/2020/util"
)

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	size := 0
	rib := 0
	for _, l := range lines {
		sides := strings.Split(l, "x")
		l, _ := strconv.Atoi(sides[0])
		w, _ := strconv.Atoi(sides[1])
		h, _ := strconv.Atoi(sides[2])
		rib += ribbonNeed(l, w, h)
		size += paperNeed(l, w, h)
	}

	fmt.Println("Step 1", size)
	fmt.Println("Step 2", rib)
}

func paperNeed(l, w, h int) int {
	s := min(l*w, w*h, h*l)
	t := (2 * l * w) + (2 * w * h) + (2 * h * l) + s
	return t
}

func ribbonNeed(l, w, h int) int {
	v := l * w * h
	c := 2 * min(l+w, w+h, h+l)
	return v + c
}

func min(nums ...int) int {
	m := nums[0]
	for _, n := range nums {
		if n < m {
			m = n
		}
	}

	return m
}
