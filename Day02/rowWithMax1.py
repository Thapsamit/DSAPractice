class Solution:

	def rowWithMax1s(self,arr, n, m):
	    idx = -1
	    maxOne = 0
	    for r in range(0,n,1):
	        totalOne = 0
	        for c in range(0,m,1):
	            if arr[r][c]==1:
	                totalOne+=1
	        if totalOne>maxOne:
	            idx = r
	            maxOne = totalOne
	    return idx