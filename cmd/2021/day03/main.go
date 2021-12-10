package main

import (
	"flag"
	"fmt"
	"log"

	"github.com/pubkraal/Advent/pkg/input"
)

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}

	lines := input.GetLines(args[0])

	fmt.Println(lines)
}
