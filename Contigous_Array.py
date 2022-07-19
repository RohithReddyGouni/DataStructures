class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        Map={0:-1};
        running_sum=0;
        max_length=0;
        for i in range(len(nums)):
            if nums[i]==0:
                running_sum-=1;
            else:
                running_sum+=1;
            if running_sum not in Map:
                Map[running_sum]=i;
            max_length=max(max_length,i-Map[running_sum]);
        return max_length;