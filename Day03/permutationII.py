from collections import defaultdict
class Solution:
    def permute(self,dm,ans,perm,n):
        if len(perm)==n:
            ans.append(perm.copy())
            return 
        for i in dm:
            if dm[i]>0:
                perm.append(i)
                dm[i]-=1
                self.permute(dm,ans,perm,n)
                dm[i]+=1
                perm.pop()
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dm = defaultdict(lambda:0)
       
        for i in nums:
            dm[i]+=1
        ans = []
        perm = []
       
        self.permute(dm,ans,perm,len(nums))
        return ans
        