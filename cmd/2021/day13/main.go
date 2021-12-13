package main

import (
	"flag"
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"

	"github.com/pubkraal/Advent/pkg/input"
)

var (
	re = regexp.MustCompile(`(y|x)=(\d+)$`)
)

type Dot struct {
	X int
	Y int
}

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}

	dots := make(map[Dot]bool)
	var instructions []string
	dodots := true

	for _, line := range input.GetLines(args[0]) {
		if line == "" {
			dodots = false
			continue
		}
		if dodots {
			parts := strings.Split(line, ",")
			d := Dot{}
			d.X, _ = strconv.Atoi(parts[0])
			d.Y, _ = strconv.Atoi(parts[1])
			dots[d] = true
		} else {
			instructions = append(instructions, line)
		}
	}

	p1 := 0
	for idx, instruction := range instructions {
		dots = fold(dots, instruction)
		if idx == 0 {
			p1 = len(dots)
		}
	}

	fmt.Println("2021:13:1 =", p1)
	fmt.Println("2021:13:2 =")
	printGrid(dots)
}

func fold(dots map[Dot]bool, instruction string) map[Dot]bool {
	parts := strings.Split(re.FindString(instruction), "=")
	f := parts[0]
	line, _ := strconv.Atoi(parts[1])

	newdots := make(map[Dot]bool)
	for dot := range dots {
		val := dot.X
		if f == "y" {
			val = dot.Y
		}
		if val < line {
			newdots[dot] = true
		} else {
			offset := line * 2
			ndot := Dot{dot.X, dot.Y}
			if f == "x" {
				ndot.X = offset - ndot.X
			} else {
				ndot.Y = offset - ndot.Y
			}
			newdots[ndot] = true
		}
	}
	return newdots
}

func printGrid(dots map[Dot]bool) {
	max := findMaxSize(dots)
	maxx := max[0]
	maxy := max[1]

	for y := 0; y <= maxy; y++ {
		for x := 0; x <= maxx; x++ {
			d := Dot{X: x, Y: y}
			if _, ok := dots[d]; ok {
				fmt.Print("#")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
}

func findMaxSize(dots map[Dot]bool) [2]int {
	maxx := 0
	maxy := 0

	for dot := range dots {
		if dot.X > maxx {
			maxx = dot.X
		}
		if dot.Y > maxy {
			maxy = dot.Y
		}
	}

	return [2]int{maxx, maxy}
}
