#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        runningSum=0;
        Map={0:1}
        count=0;
        for i in range(len(nums)):
            runningSum+=nums[i];
            Array_difference=runningSum-k;
            if Array_difference in Map:
                count+=Map[Array_difference];
            if runningSum not in Map:
                Map[runningSum]=1;
            else:
                Map[runningSum]+=1;
                     
        return count; 