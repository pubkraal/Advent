package main

import "testing"

func TestGetSeat(t *testing.T) {
	table := []struct {
		ID   string
		row  int
		seat int
	}{
		{"BFFFBBFRRR", 70, 7},
		{"FFFBBBFRRR", 14, 7},
		{"BBFFBBFRLL", 102, 4},
		{"FBFBBFFRLR", 44, 5},
	}

	for _, row := range table {
		res := getSeat(row.ID)
		if res.Row != row.row || res.Seat != row.seat {
			t.Errorf("getSeat(%s) = %v. Expected %v",
				row.ID, res, Seat{Row: row.row, Seat: row.seat})
		}
	}
}

func TestSeatID(t *testing.T) {
	table := []struct {
		row    int
		seat   int
		expect int
	}{
		{44, 5, 357},
		{70, 7, 567},
		{14, 7, 119},
		{102, 4, 820},
	}

	for _, row := range table {
		s := Seat{Row: row.row, Seat: row.seat}
		res := s.SeatID()
		if res != row.expect {
			t.Errorf("%v.SeatID() = %v. Expect %v",
				s, res, row.expect)
		}
	}
}
