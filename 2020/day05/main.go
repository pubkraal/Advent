package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/pubkraal/Advent/2020/util"
)

type Seat struct {
	Row  int
	Seat int
}

func (s Seat) SeatID() int {
	return (s.Row * 8) + s.Seat
}

func main() {
	lines, err := util.GetLines("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	seatmap := make(map[int]bool)

	minCode := 9000
	maxCode := 0

	for _, line := range lines {
		seatid := getSeat(line).SeatID()
		if seatid > maxCode {
			maxCode = seatid
		}
		if seatid < minCode {
			minCode = seatid
		}
		seatmap[seatid] = true
	}

	fmt.Println("Step 1:", maxCode)

	for i := minCode; i < maxCode; i++ {
		_, ok := seatmap[i]
		if !ok {
			fmt.Println("Step 2:", i)
			break
		}
	}
}

func getSeat(line string) Seat {
	r := strings.NewReplacer("B", "1", "R", "1", "F", "0", "L", "0")
	rline := r.Replace(line)

	row, _ := strconv.ParseInt(rline[:7], 2, 64)
	seat, _ := strconv.ParseInt(rline[7:], 2, 64)

	return Seat{Row: int(row), Seat: int(seat)}
}
