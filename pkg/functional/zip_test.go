package functional

import (
	"reflect"
	"testing"
)

func TestZipInt(t *testing.T) {
	table := []struct {
		name   string
		list1  []int
		list2  []int
		expect [][]int
	}{
		{
			"Simple case",
			[]int{1, 2, 3},
			[]int{4, 5, 6},
			[][]int{{1, 4}, {2, 5}, {3, 6}},
		},
		{
			"First list longer",
			[]int{1, 2, 3, 7, 8, 9},
			[]int{4, 5, 6},
			[][]int{{1, 4}, {2, 5}, {3, 6}},
		},
		{
			"Second list longer",
			[]int{1, 2, 3},
			[]int{4, 5, 6, 7, 8, 9},
			[][]int{{1, 4}, {2, 5}, {3, 6}},
		},
		{
			"First list longer",
			[]int{1, 2, 3, 4, 5},
			[]int{2, 3, 4, 5},
			[][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}},
		},
	}

	for _, row := range table {
		tc := row
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()
			res := ZipInt(row.list1, row.list2)
			if !reflect.DeepEqual(row.expect, res) {
				t.Errorf("ZipInt(%v, %v) = %v. Want %v", row.list1, row.list2, res, row.expect)
			}
		})
	}
}
