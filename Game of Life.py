#Time Complexity: O(n2)
#Space Complexity: O(1)


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #original| New | State
        #    0   |  0  |   0
        #    1   |  0  |   1
        #    0   |  1  |   2
        #    1   |  1  |   3
        Rows=len(board);
        Columns=len(board[0]);
        def neighbours(row,column):
            neighbourCount=0;
            for i in range(row-1,row+2):
                for j in range(column-1,column+2):
                    if  i<0 or j<0 or (i==Rows or j==Columns) or (i==row and j==column):
                        continue;
                    if board[i][j] in [1,3]:
                        neighbourCount+=1;
            return neighbourCount;
            
        for i in range(Rows):
            for j in range(Columns):
                State=neighbours(i,j);
                if board[i][j]:
                    if State in [2,3]:
                        board[i][j]=3;
                else:
                    if State in [3]:
                        board[i][j]=2;
        for i in range(Rows):
            for j in range(Columns):
                if board[i][j] in [2,3]:
                    board[i][j]=1;
                elif board[i][j]==1:
                    board[i][j]=0;
                    
                        
                
        
                
                    
                
        
        
        