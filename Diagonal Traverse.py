# Time Complexity: O(no.of rows*no.of columns)
# Space Complexity: O(1)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result=[];
        m=len(mat);
        n=len(mat[0]);
        row=0;
        col=0;
        count=m*n;
        while count >0:
            result.append(mat[row][col]);
            r=row;
            c=col;
            if (row+col)%2==0:
                if row > 0:
                    row=row-1;
                else:
                    row=0;
                col=col+1
            else:
                if col>0:
                    col=col-1;
                else:
                    col=0;
                row=row+1;
            if col>=n:
                row=r+1;
                col=c;
            elif row>=m:
                col=c+1;
                row=r;
            count-=1;
        return result;
                