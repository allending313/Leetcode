func twoSum(numbers []int, target int) []int {
    for l, r := 0, len(numbers) - 1 ;; {
        switch {
            case numbers[l] + numbers[r] > target: 
                r--
            case numbers[l] + numbers[r] < target:
                l++
            default:
                return []int{l+1, r+1}
        }
    }
}