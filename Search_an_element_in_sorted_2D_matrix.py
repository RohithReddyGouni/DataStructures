# Time Complexity: O(logn)

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
                