func maxProfit(prices []int) int {
    var profit = 0
    var minPrice = prices[0]
    
    for i := 1; i < len(prices); i++ {
        if prices[i] < minPrice {
            minPrice = prices[i]
        } else if (prices[i] - minPrice) > profit {
            profit = prices[i] - minPrice
        }
    }
    
    return profit
}