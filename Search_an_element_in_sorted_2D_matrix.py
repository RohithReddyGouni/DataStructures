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





// Search an element in a sorted 2D matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = m*n-1
        
        while low <= high:
            mid = low + (high - low)//2
            r = mid//n
            c = mid%n
            #print(matrix[r][c])
            
            if matrix[r][c] == target:
                return True
            
            elif matrix[r][c] > target:
                high = mid -1
                
            else:
                low = mid + 1
                
        return False
                