#Time Complexity: O(no.of rows*no.of columns)
#Space Complexity: O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[];
        left=0;
        right=len(matrix[0]);
        top=0;
        bottom=len(matrix);
        row=0;
        col=0;
        while top < bottom and left < right:
            for i in range(left, right):
                result.append(matrix[top][i]);
            top+=1;
            for i in range(top,bottom):
                result.append(matrix[i][right-1]);
            right-=1;
            
            if not (left<right and top<bottom):
                break;
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i]);
            bottom-=1;
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left]);
            left+=1;
        return result;