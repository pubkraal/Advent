package main

import (
	"errors"
	"flag"
	"log"
	"strconv"
	"strings"

	"github.com/pubkraal/Advent/pkg/input"
)

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}

	lines := input.GetLines(args[0])

	var x int64 = 0
	var y int64 = 0
	var y2 int64 = 0

	for _, line := range lines {
		parts := strings.Split(line, " ")
		num, err := strconv.ParseInt(parts[1], 10, 32)
		if err != nil {
			panic(err)
		}
		switch parts[0] {
		case "forward":
			x += num
			y2 += int64(y * num)
		case "down":
			y += num
		case "up":
			y -= num
		default:
			panic(errors.New("unnown direction: " + parts[0]))
		}
	}

	log.Println("2021:02:1 =", x*y)
	log.Println("2021:02:2 =", int64(x)*y2)
}
