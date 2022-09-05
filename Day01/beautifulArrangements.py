class Solution:
    def dfs(self,nums,val,n,res):
        if val>n:
            res[0]+=1
            return
        for i in range(1,n+1,1):
            if nums[i]==0 and (val%i==0 or i%val==0):
                nums[i] = val
                self.dfs(nums,val+1,n,res)
                nums[i] =  0
        
    def countArrangement(self, n: int) -> int:
        res = [0]
        nums = [0 for i in range(n+1)]
        self.dfs(nums,1,n,res)
        return res[0]
        
        