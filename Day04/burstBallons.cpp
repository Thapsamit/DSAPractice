class Solution{
public:
    long long int maxProductSum(int N, int nums[])
    {
        int n = N;
        vector<vector<long long int>> dp(n,vector<long long int>(n,0));
        for(int g=0;g<n;g++){
            for(int i=0,j=g;j<n;i++,j++){
                long long int maxCost = LLONG_MIN;
                for(int k = i; k<=j; k++){
                    long long int left = k==i?0:dp[i][k-1];
                    long long int right = k==j?0:dp[k+1][j];
                    long long int val = nums[k];
                    if(i>0){
                        val = nums[i-1]*val;
                    }
                    if(j!=n-1){
                        val = val*nums[j+1];
                    }
                    long long int tot = left+right+val;
                    if(tot>maxCost){
                        maxCost = tot;
                    }
                }
                dp[i][j] = maxCost;
            }
        }
        return dp[0][n-1];
    }
};