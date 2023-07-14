func removeElement(nums []int, val int) int {

    /* two pointer solution, first attempt

    head, tail := 0, len(nums) - 1
    for tail >= head {
        if nums[head] == val {
            if nums[tail] != val {
                nums[head] = nums[tail]
                head++
            }
            tail--
        } else {
            head++
        }
    }
    return head

    */

    // no need for two pointers...
    i := 0
    for _, v := range nums {
        if v != val {
            nums[i] = v
            i++
        }
    }
    return i
}