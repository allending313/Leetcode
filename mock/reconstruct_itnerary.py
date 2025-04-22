class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for x, y in tickets:
            graph[x].append(y)
        
        for k in graph.keys():
            graph[k].sort(reverse=True)
        
        stack = ["JFK"]
        res = []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                res.append(stack.pop())
        
        return res[::-1]