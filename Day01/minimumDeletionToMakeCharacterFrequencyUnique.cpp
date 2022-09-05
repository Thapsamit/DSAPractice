#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minDeletions(string s) {
         vector<int>freq(26);
         for(auto ch:s){
             freq[ch-'a']+=1;
         }
        sort(freq.begin(),freq.end(),greater<int>());
        
        int maxF = freq[0]; //get maximum permissible frequency
        int res = 0;
        for(auto val:freq){
            // if value is greater than maxF then only delete otherwise go ahead
            if(val>maxF){
                if(maxF>0){
                   res+=(val-maxF); 
                }
                else{
                    res+=val;
                }
            }
            maxF = min(maxF-1,val-1);
        }
        return res;
         
        
    }
};