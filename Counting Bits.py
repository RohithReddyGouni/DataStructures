#Time Complexity: O(n)

class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[0]*(n+1);
        output[0]=0;
        offset=1;
        for i in range(1,n+1):
            if 2*offset==i:
                offset=i;
            output[i]=1+output[i-offset];
        return output;