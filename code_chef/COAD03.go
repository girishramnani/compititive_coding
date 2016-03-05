package main

import "fmt"

func main() {
	// intialization
	var cases, island int
	var ans = make([]int, 1001)
	ans[1] = 1
	ans[2] = 2

	// precomputation
	for i := 3; i < 1001; i++ {
		if i%2 == 0 {
			ans[i] = ans[i/2] + 2
		} else {
			ans[i] = ans[i-1] + 1
		}
	}

	fmt.Scanf("%d", &cases)
	for ; cases > 0; cases-- {
		fmt.Scanf("%d", &island)
		fmt.Println(ans[island])
	}

}
