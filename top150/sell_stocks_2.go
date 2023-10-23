func maxProfit(prices []int) int {
    profit := 0
    for i := 0; i < len(prices) - 1; i++ {
        if gain := prices[i+1] - prices[i]; gain > 0 {
            profit += gain
        }
    }
    return profit
}