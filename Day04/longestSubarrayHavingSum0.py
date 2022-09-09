from collections import defaultdict
class Solution:
    def maxLen(self, n, arr):
        dm = defaultdict(lambda:0)
        dm[0] = -1
        maxLen = 0
        tot = 0
        for i in range(0,n,1):
            tot+=arr[i]
            if tot in dm:
                maxLen = max(maxLen,i-dm[tot])
            else:
                dm[tot] = i
        return maxLen