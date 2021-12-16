package math

import "testing"

func TestMinInt(t *testing.T) {
	table := []struct {
		name      string
		inputlist []int
		expect    int
	}{
		{"simple ascending", []int{1, 2, 3, 4, 5}, 1},
		{"simple descending", []int{5, 4, 3, 2, 1}, 1},
		{"random numbers", []int{-12, 32423, 234, 54}, -1},
	}

	for _, tc := range table {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()
			r := MinInt(tc.inputlist)
			if r != tc.expect {
				t.Errorf("MinInt(%v) == %v. Want %v", tc.inputlist, r, tc.expect)
			}
		})
	}

}
