package main

import "testing"

func TestPaperNeed(t *testing.T) {
	table := []struct {
		l   int
		w   int
		h   int
		exp int
	}{
		{2, 3, 4, 58},
		{1, 1, 10, 43},
	}

	for _, row := range table {
		res := paperNeed(row.l, row.w, row.h)
		if res != row.exp {
			t.Errorf("paperNeed(%v) = %v, expected %v", row, res, row.exp)
		}
	}
}

func TestRibbonNeed(t *testing.T) {
	table := []struct {
		l   int
		w   int
		h   int
		exp int
	}{
		{2, 3, 4, 34},
		{1, 1, 10, 14},
	}

	for _, row := range table {
		res := ribbonNeed(row.l, row.w, row.h)
		if res != row.exp {
			t.Errorf("ribbonNeed(%v) = %v. expected %v", row, res, row.exp)
		}
	}
}

func TestMin(t *testing.T) {
	table := []struct {
		nums []int
		exp  int
	}{
		{[]int{1, 2, 3, 4}, 1},
		{[]int{64, 323, 542, 3129}, 64},
		{[]int{-231, 34, 52344, 1232}, -231},
	}

	for _, row := range table {
		res := min(row.nums...)
		if res != row.exp {
			t.Errorf("min(%v) = %v. Expected %v", row.nums, res, row.exp)
		}
	}
}
