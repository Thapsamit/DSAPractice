class Solution:
    def isPalindrome(self,s,i,j):
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def partPal(self,i,s,res,part):
        if i>=len(s):
            res.append(part.copy())
            return
        for j in range(i,len(s),1):
            if self.isPalindrome(s,i,j):
                part.append(s[i:j+1])
                self.partPal(j+1,s,res,part)
                part.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        self.partPal(0,s,res,part)
        return res
        