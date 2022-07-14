#Time Complexity: O(m+n) - If 'm' is greater than 'n' then the time complexity is O(m) else O(n) 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0;
        col=len(matrix[row])-1;

        while row < len(matrix) and col>=0:
            
                if target == matrix[row][col]:
                    return True;
                if target < matrix[row][col]:
                    col=col-1;
                else:
                    row=row+1;
        return False;