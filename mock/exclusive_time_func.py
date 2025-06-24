class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # intuition: using a stack to keep track of current exec
        # at each log: increment exclusive time of top id on the stack
        # at each start log: append new time 0 onto res
        # at each end log: clear top stack

        res = []
        stack = []
        
        for log in logs:
            log = log.split(':')
            fid, start, time = int(log[0]), log[1] == 'start', int(log[2])
            if not start:
                time += 1
                
            if stack:
                prev = stack[-1]
                res[prev[0]] += time - prev[2]
                
            if start:
                stack.append([fid, start, time])
                if len(res) <= fid:
                    res.append(0)
            else:
                stack.pop()
                if stack:
                    stack[-1][2] = time
        
        return res