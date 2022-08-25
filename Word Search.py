class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board=board
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if self.dfs(i,j,m,n,0,word):
                        return True
        return False
    def dfs(self,i,j,m,n,index,word):
        if index==len(word):
            return True
        if i<0 or i==m or j<0 or j==n or self.board[i][j]=="#":
            return False
        if self.board[i][j]==word[index]:
            self.board[i][j]="#"
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                nr=dx+i
                nc=dy+j
                if self.dfs(nr,nc,m,n,index+1,word):
                    return True
            self.board[i][j]=word[index]
        return False