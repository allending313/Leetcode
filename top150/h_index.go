import (
    "sort"
    "fmt"
)

/* initial approach

func hIndex(citations []int) int {
    res := 0
    sort.Sort(sort.Reverse(sort.IntSlice(citations)))
    
    for i, v := range citations {
        if v >= i + 1 {
            res = i + 1
        } else {
            break
        }
    }
    return res
}

*/

func hIndex(citations []int) int {
    sort.Ints(citations)
    for i := 0; i < len(citations); i++{
        if citations[i] >= len(citations) - i  {
            return len(citations) - i
        }
    }
    return 0
}
