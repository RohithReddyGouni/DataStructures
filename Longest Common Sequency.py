#Time Complexity: O(m*n)
#Space Complexity: O(m*n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1);
        n=len(text2);
        dp=[[None for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0;
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1];
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
        return dp[-1][-1]; 