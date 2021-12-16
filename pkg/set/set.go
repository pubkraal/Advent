package set

type IntSet struct {
	values map[int]bool
}

type Set interface {
	Add(int)
	Clear()
	Remove(int)
	Contains(int) bool
	Difference(*Set) Set
	Intersection(*Set) Set
	Union(*Set) Set
	Equals(*Set) bool
}

func NewIntSet() *IntSet {
	return &IntSet{values: make(map[int]bool)}
}

func FromIntList(vals ...int) *IntSet {
	is := &IntSet{values: make(map[int]bool)}
	is.AddList(vals...)
	return is
}

func (s *IntSet) Add(val int) {
	s.values[val] = true
}

func (s *IntSet) AddList(val ...int) {
	for _, v := range val {
		s.values[v] = true
	}
}

func (s *IntSet) Clear() {
	s.values = make(map[int]bool)
}

func (s *IntSet) Remove(val int) {
	delete(s.values, val)
}

func (s *IntSet) Contains(val int) bool {
	_, ok := s.values[val]
	return ok
}

// Difference returns a new Set with elements in s but not in cmp
func (s *IntSet) Difference(cmp *IntSet) *IntSet {
	ns := NewIntSet()
	for k := range s.values {
		if !cmp.Contains(k) {
			ns.Add(k)
		}
	}
	return ns
}

// Intersection returns a new Set with all elements present in both sets
func (s *IntSet) Intersection(cmp *IntSet) *IntSet {
	return s
}

// Union returns a new Set with all the elements in either set
func (s *IntSet) Union(cmp *IntSet) *IntSet {
	ns := &IntSet{values: make(map[int]bool)}
	for k := range s.values {
		if cmp.Contains(k) {
			ns.Add(k)
		}
	}
	return ns
}

func (s *IntSet) Equals(cmp *IntSet) bool {
	for k := range s.values {
		if !cmp.Contains(k) {
			return false
		}
	}
	for k := range cmp.values {
		if !s.Contains(k) {
			return false
		}
	}
	return true
}

func (s *IntSet) Values() []int {
	r := make([]int, 0)
	for k := range s.values {
		r = append(r, k)
	}
	return r
}
