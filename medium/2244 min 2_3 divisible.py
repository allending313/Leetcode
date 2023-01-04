def minimumRounds(self, tasks: List[int]) -> int:
    counter = Counter(tasks)
    res = 0
    for val in counter.values():
        if val == 1:
            return -1
        res += ceil(val/3)
    return res