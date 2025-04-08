class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # seen = set()
        
        # def backtrack(path, used): 
        #     if path != "" and path not in seen:
        #         seen.add(path)
            
        #     for i, x in enumerate(tiles):
        #         if used[i]:
        #             continue
        
        #         used[i] = True
        #         path += tiles[i]
        #         backtrack(path, used)
        #         path = path[:-1]
        #         used[i] = False
        
        # backtrack("", [False] * len(tiles))
        # return len(seen)

        letter_count = collections.Counter(tiles)

        def dfs():
            count = 0
            for tile in letter_count:
                if letter_count[tile] == 0:
                    continue
                letter_count[tile] -= 1
                count += dfs() + 1 
                letter_count[tile] += 1
            return count   
        return dfs()