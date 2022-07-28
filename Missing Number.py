#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0;
        for i in range(len(nums)+1):
            sum+=i;
        for j in nums:
            sum-=j;
        return sum;