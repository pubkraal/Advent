package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"

	"github.com/pubkraal/Advent/2020/util"
)

var ire *regexp.Regexp

func init() {
	var err error
	ire, err = regexp.Compile(`(\w+) ([+\-]\d+)`)
	if err != nil {
		panic(err)
	}
}

type Instruction struct {
	Act   string
	Val   int
	Count int
}

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	is := make([]*Instruction, len(lines))

	swap := make([]int, 0)

	for idx, line := range lines {
		inst := FromString(line)
		is[idx] = inst

		if inst.Act == "jmp" || inst.Act == "nop" {
			swap = append(swap, idx)
		}
	}

	acc, _ := run(is, -1)

	fmt.Println("Step 1:", acc)
	var bail bool

	for _, swappos := range swap {
		reset(is)
		acc, bail = run(is, swappos)
		if !bail {
			break
		}
	}

	fmt.Println("Step 2:", acc, bail)
}

func reset(is []*Instruction) {
	for _, i := range is {
		i.Count = 0
	}
}

func run(is []*Instruction, modify int) (int, bool) {
	acc := 0
	ip := 0
	for {
		// Exit condition 1: end of program reached
		if ip >= len(is) || ip < 0 {
			break
		}

		i := is[ip]

		// Exit condition 2: same instruction reached
		if i.Count > 0 {
			return acc, true
		}

		// Execute instruction
		act := i.Act
		if ip == modify {
			switch i.Act {
			case "jmp":
				act = "nop"
			case "nop":
				act = "jmp"
			}
		}

		switch act {
		case "acc":
			acc += i.Val
			ip++
		case "jmp":
			ip += i.Val
		case "nop":
			ip++
		default:
			log.Fatalf("Ran into unknown instruction %v", i)
		}
		i.Count++
	}
	return acc, false
}

func FromString(line string) *Instruction {
	m := ire.FindAllStringSubmatch(line, -1)
	v, err := strconv.Atoi(m[0][2])
	if err != nil {
		panic(err)
	}

	i := &Instruction{
		Count: 0,
		Act:   m[0][1],
		Val:   v,
	}

	return i
}
