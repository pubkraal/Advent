package main

import (
	"flag"
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/pubkraal/Advent/pkg/functional"
	"github.com/pubkraal/Advent/pkg/input"
	"github.com/pubkraal/Advent/pkg/math"
	"github.com/pubkraal/Advent/pkg/set"
)

type Board struct {
	numbers [][]int
}

func main() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 1 {
		log.Fatal("Not enough arguments. Give input file.")
	}

	draws := make([]int, 0)
	boards := make([]Board, 0)

	data := input.GetLines(args[0])

	for _, num := range strings.Split(data[0], ",") {
		inum, _ := strconv.Atoi(num)
		draws = append(draws, inum)
	}

	for i := 0; i < len(data)/6; i++ {
		board := Board{}
		lines := data[i*6+2 : i*6+7]
		for _, line := range lines {
			nums := filterEmpty(strings.Split(line, " "))
			board.numbers = append(board.numbers, toIntSlice(nums))
		}
		boards = append(boards, board)
	}

	winners := findWinners(boards, draws)

	fmt.Println("2021:04:1 =", winners[0])
	fmt.Println("2021:04:2 =", winners[len(winners)-1])
}

func findWinners(boards []Board, draws []int) []int {
	winners := make([]int, 0)
	for i := 0; i < len(draws)-5; i++ {
		called := draws[:i+5]

		win_round := make([]int, 0)
		for i, brd := range boards {
			win := checkWinner(brd, called)
			if len(win) > 0 {
				winners = append(winners, math.SumInt(win)*called[len(called)-1])
				win_round = append(win_round, i)
			}
		}

		for i := len(win_round) - 1; i >= 0; i-- {
			pos := win_round[i]
			boards = popBoard(boards, pos)
		}
	}
	return winners
}

func checkWinner(board Board, draws []int) []int {
	rows := make([][]int, 0)
	rows = append(rows, board.numbers...)
	rows = append(rows, functional.ZipInt(board.numbers...)...)

	picked := set.NewIntSet()
	picked.AddList(draws...)

	for _, r := range rows {
		row := set.FromIntList(r...)
		if row.Union(picked).Equals(row) {
			bs := set.NewIntSet()
			for _, x := range board.numbers {
				bs.AddList(x...)
			}
			unmarked := bs.Difference(picked)
			return unmarked.Values()
		}
	}

	return []int{}
}

func popBoard(in []Board, pos int) []Board {
	return append(in[:pos], in[pos+1:]...)
}

func toIntSlice(in []string) []int {
	ret := make([]int, len(in))
	for idx, v := range in {
		n, _ := strconv.Atoi(v)
		ret[idx] = n
	}
	return ret
}

func filterEmpty(in []string) []string {
	ret := make([]string, 0)
	for _, x := range in {
		if x == "" {
			continue
		}
		ret = append(ret, x)
	}
	return ret
}
