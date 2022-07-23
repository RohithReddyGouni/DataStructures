#Time Complexity - O(n2)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        matrix=[[None for i in range((amount+1))] for j in range(len(coins)+1)]
        for i in range(len(matrix)):
            matrix[i][0]=0;
        for i in range(1,amount+1):
            matrix[0][i]=amount+1;
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if j<coins[i-1]:
                    matrix[i][j]=matrix[i-1][j];
                else:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-coins[i-1]]+1)
        if matrix[-1][-1]==amount+1:
            return -1;
        else:
            return matrix[-1][-1];