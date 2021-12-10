package main

import (
	"errors"
	"flag"
	"log"
	"sort"

	"github.com/pubkraal/Advent/pkg/input"
)

var OPEN []rune = []rune{'(', '[', '{', '<'}
var CLOSE []rune = []rune{')', ']', '}', '>'}
var POINTS map[rune]int = map[rune]int{')': 3, ']': 57, '}': 1197, '>': 25137}
var COMPLETIONPOINTS map[rune]int = map[rune]int{'(': 1, '[': 2, '{': 3, '<': 4}

type RuneStack []rune

func (s RuneStack) Push(r rune) RuneStack {
	return append(s, r)
}

func (s RuneStack) Pop() (RuneStack, rune) {
	l := len(s)
	if l == 0 {
		panic(errors.New("cannot pop from empty stack"))
	}

	return s[:l-1], s[l-1]
}

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}

	var p1 int64 = 0
	var p2 []int

	for _, line := range input.GetLines(args[0]) {
		var stack RuneStack
		corrupt := false
		for _, chr := range line {
			if inSlice(chr, OPEN) {
				stack = stack.Push(chr)
			} else {
				var last rune
				stack, last = stack.Pop()
				p, err := pos(last, OPEN)
				if err != nil {
					panic(err)
				}
				closer := CLOSE[p]
				if closer != chr {
					p1 += int64(POINTS[chr])
					corrupt = true
					break
				}
			}
		}

		if !corrupt {
			tmp := 0
			for _, x := range stack {
				tmp *= 5
				tmp += COMPLETIONPOINTS[x]
			}
			p2 = append(p2, tmp)
		}
	}

	sort.Ints(p2)

	log.Println("2021:10:1 =", p1)
	log.Println("2021:10:2 =", p2[len(p2)/2])
}

func inSlice(needle rune, haystack []rune) bool {
	for _, x := range haystack {
		if needle == x {
			return true
		}
	}
	return false
}

func pos(needle rune, haystack []rune) (int, error) {
	for idx, r := range haystack {
		if needle == r {
			return idx, nil
		}
	}
	return 0, errors.New("needle not found in haystack")
}
