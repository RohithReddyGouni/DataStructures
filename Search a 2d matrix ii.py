class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix);
        j=len(matrix[0])-1;
        i=0;
        while i < len(matrix):
            
                if j<0 or i > row-1:
                    return False;
                
                elif target==matrix[i][j]:
                    return True;
                
                else:
                    
                    if matrix[i][j]<target:
                        i+=1;
                    elif matrix[i][j]>target:
                        j-=1;
        return False;