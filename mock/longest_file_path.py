class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Create a stack containing the lengths of each of the path components 
        # along with a running total of the component lengths.
        # Depth in the filepath is based on how many tab characters per line.

        input = input.split('\n')
        path, ans, total = [], 0, 0
    
        for line in input:
            tabs = line.count('\t')

            while len(path) > tabs:
                total -= path.pop()
    
            path.append(len(line) - tabs)
            total += path[-1]

            # file found
            if '.' in line:
                ans = max(ans, total + len(path) - 1)

        return ans