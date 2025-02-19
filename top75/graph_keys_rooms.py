class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [*rooms[0]]
        rooms[0] = [-1]

        while keys:
            key = keys.pop()
            if rooms[key] and rooms[key][0] != -1:
                keys.extend(rooms[key])
            rooms[key] = [-1]
        
        return all(x == [-1] for x in rooms)
