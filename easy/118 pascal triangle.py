class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
            
        def pascal(arr):
            out = [0] * (len(arr) + 1)
            for i, x in enumerate(arr):
                out[i] += x
                out[i+1] += x
            return out
        
        res = []
        for i in range(numRows):
            if i == 0:
                arr = [1]
            else:
                arr = pascal(arr)
            res.append(arr)

        return res