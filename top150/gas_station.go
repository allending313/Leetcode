func canCompleteCircuit(gas, cost []int) int {
    start, total, tank := 0, 0, 0

    for i := 0; i < len(gas); i++ {
        if tank += gas[i] - cost[i]; tank < 0 {
            start, total, tank = i + 1, total + tank, 0
        }
    }

    if (total + tank < 0) { 
        return -1 
    }

    return start
}

// could also achieve solution by finding maxSubArray of the difference of gas - cost via Kadane's Algorithm