package util

import (
	"reflect"
	"testing"
)

func TestCombinations(t *testing.T) {
	tables := []struct {
		input  []int
		size   int
		expect [][]int
	}{
		{input: []int{0, 1, 2, 3}, size: 3, expect: [][]int{
			{0, 1, 2},
			{0, 1, 3},
			{0, 2, 3},
			{1, 2, 3}}},
		{input: []int{0, 1}, size: 3, expect: [][]int{}},
	}
	for _, row := range tables {
		res := Combinations(row.input, row.size)
		if !reflect.DeepEqual(res, row.expect) {
			t.Errorf("Combinations(%v, %v) == %v. Expected %v", row.input, row.size, res, row.expect)
		}
	}
}

func TestCombination(t *testing.T) {
	pool := []int{0, 1, 2, 3, 4}
	tables := []struct {
		indices []int
		expect  []int
	}{
		{indices: []int{0, 1}, expect: []int{0, 1}},
		{indices: []int{1, 2}, expect: []int{1, 2}},
		{indices: []int{4, 3}, expect: []int{4, 3}},
	}

	for _, row := range tables {
		res := combination(pool, row.indices)
		if !reflect.DeepEqual(row.expect, res) {
			t.Errorf("combination(%v, %v) = %v. Expected %v", pool, row.indices, res, row.expect)
		}
	}
}

func TestRange(t *testing.T) {
	nums := Range(3)
	expect := []int{0, 1, 2}
	if !reflect.DeepEqual(nums, expect) {
		t.Errorf("Range(3) = %v. Expected %v", nums, expect)
	}
}

func TestStartRange(t *testing.T) {
	nums := StartRange(4, 10)
	expect := []int{4, 5, 6, 7, 8, 9}
	if !reflect.DeepEqual(nums, expect) {
		t.Errorf("StartRange(4, 10) = %v. Expected %v", nums, expect)
	}
}
