func candy(ratings []int) int {
    // l := len(ratings)
    // res := 0
    // candies := make([]int, l)
   

    // // Give one candy for each child
    // for i :=0 ; i < l; i ++ {
    //     candies[i] = 1
    // }

    // // Check left -> right
    // for i := 1; i < l; i ++ {
    //     if ratings[i] > ratings[i-1] {
    //         candies[i] = candies[i-1] + 1
    //     }
    // }

    // // Check right -> left
    // for i := l - 2; i >= 0 ; i -- {
    //     if ratings[i] > ratings[i+1] && candies[i] <= candies[i+1] {
    //         candies[i] = candies[i+1] + 1
    //     }
    // }

    // for i := 0; i < l; i ++ {
    //     res += candies[i]
    // }

    // return res

    if len(ratings) == 0 {
        return 0
    }

    res, up, down, peak := 1, 0, 0, 0

    for i := 0; i < len(ratings) - 1; i++ {
        prev, curr := ratings[i], ratings[i+1]

        if prev < curr {
            up++
            down = 0
            peak = up
            res += 1 + up
        } else if prev == curr {
            up, down, peak = 0, 0, 0
            res += 1
        } else {
            up = 0
            down++
            res += 1 + down
            if peak >= down {
                res--
            }
        }
    }

    return res
}