package main

import "fmt"

func main() {
	var a, temp int
	// fmt.Scanf("%d", &a)
	a = 4
	var arr = make([]int, a)
	for i := 0; i < a; i++ {

		fmt.Scanf("%d", &temp)
		arr[i] = temp

	}
	arr = []int{1, 2, 1, 2}

	var winners = make([]int, a+1)
	var sum []int
	dnum, dcount := 0, 0 //consider using inf for dnum
	for i := 0; i < a; i++ {
		sum = make([]int, a+1)
		for j := i; j < a; j++ {
			temp = arr[i]
			sum[temp]++
			if sum[temp] == dcount {
				if temp < dnum {
					winners[temp]++
				} else {
					winners[dnum]++
				}
			} else if sum[temp] > dcount {
				dcount = sum[temp]
				dnum = temp
				winners[temp]++
			}
		}
	}
}
