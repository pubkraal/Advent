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

	seats := make([]Seat, len(lines))
	seatmap := make(map[int]bool)

	minCode := 9000
	maxCode := 0

	for idx, line := range lines {
		seats[idx] = getSeat(line)
		seatid := seats[idx].SeatID()
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
	row, _ := strconv.ParseInt(
		strings.Replace(
			strings.Replace(line[0:7], "B", "1", -1),
			"F", "0", -1),
		2, 64)
	seat, _ := strconv.ParseInt(
		strings.Replace(
			strings.Replace(line[7:10], "R", "1", -1),
			"L", "0", -1),
		2, 64)

	return Seat{Row: int(row), Seat: int(seat)}
}
