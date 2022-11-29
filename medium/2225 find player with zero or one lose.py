class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        one = set()
        los = set()
        for winner, loser in matches:
            if loser in one:
                los.add(loser)
                one.remove(loser)
            elif loser in win:
                one.add(loser)
                win.remove(loser)
            elif loser not in los:
                one.add(loser)
            
            if winner not in one and winner not in los:
                win.add(winner)
                
        return [sorted(list(win)), sorted(list(one))]
    