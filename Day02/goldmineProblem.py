class Solution:
    def maxGold(self, n, m, M):
        dp = [[0 for i in range(m)] for j in range(n)]
        maxGold = -99999999
        
        for i in range(m-1,-1,-1):
            for j in range(n):
                right = 0
                diagUp = 0
                diagDown = 0 
                #right 
                if i+1<m:
                    right = dp[j][i+1]
                if j-1>=0 and i+1<m:
                    diagUp = dp[j-1][i+1]
                
                if i+1<m and j+1<n:
                    diagDown = dp[j+1][i+1]
                dp[j][i] = M[j][i] + max(right,diagUp,diagDown)
                maxGold = max(maxGold,dp[j][i])
    
        return maxGold