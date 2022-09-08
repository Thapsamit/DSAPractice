from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dm = defaultdict(lambda:0)
        for i in range(0,len(stones),1):
            dm[stones[i]] = set() # set to store unique jumps
        dm[stones[0]].add(1);
        for i in range(0,len(stones),1):
            currStone = stones[i]
            jumps = dm[currStone]
            print(jumps)
            for jump in jumps:
                pos = currStone+jump
                if pos==stones[len(stones)-1]:
                    return True
                if pos in dm:
                    if jump-1>0:
                        dm[pos].add(jump-1);
                    dm[pos].add(jump);
                    dm[pos].add(jump+1);
        return False
            
        