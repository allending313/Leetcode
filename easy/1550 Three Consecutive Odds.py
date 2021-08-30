"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
"""
def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    counter = 0
    for x in arr:
        if x%2 == 0:
            counter = 0
        else:
            counter += 1
        
        if counter == 3:
            return True
    
    return False

    # return "111" in "".join([str(i%2) for i in arr])