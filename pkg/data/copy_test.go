package data

import (
	"reflect"
	"testing"
)

func TestCopyCheapSet(t *testing.T) {
	t1 := make(map[string]bool)
	t1["test"] = true
	t1["beepboop"] = false
	table := []struct {
		name   string
		in     map[string]bool
		expect map[string]bool
	}{
		{name: "Simple Cheap Set Copy", in: t1, expect: t1},
	}

	for _, tc := range table {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()
			c := CopyCheapSet(tc.in)
			if !reflect.DeepEqual(c, tc.expect) {
				t.Errorf("CopyCheapSet(%v) == %v. Want %v", tc.in, c, tc.expect)
			}
		})
	}
}
