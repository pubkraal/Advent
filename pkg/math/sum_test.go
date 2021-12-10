package math

import "testing"

func TestSumInt(t *testing.T) {
	table := []struct {
		name   string
		in     []int
		expect int
	}{
		{"simple positive", []int{1, 2, 3}, 6},
		{"simple negative", []int{-1, -2, -3}, -6},
	}

	for _, tc := range table {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()
			r := SumInt(tc.in)
			if r != tc.expect {
				t.Errorf("SumInt(%v) = %v. Want %v", tc.in, r, tc.expect)
			}
		})
	}
}
