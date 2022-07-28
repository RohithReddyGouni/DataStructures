#Time Complexity: O(32)=>O(1)
#Space Complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0;
        for i in range(32):
            if n&1==1:
                count+=1;
            n=n>>1;
        return count;