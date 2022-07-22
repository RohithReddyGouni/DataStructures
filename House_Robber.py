#Time Complexity: O(n)  => n=100
#Space Complexity: O(n) => n=100


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0];
        amount=[];
        amount.append(nums[0]);
        amount.append(max(nums[1],nums[0]));
        for i in range(2,len(nums)):
            Max=max(amount[i-2]+nums[i],amount[i-1])
            amount.append(Max)
        if amount[-1]> amount[-2]:
            return amount[-1];
        else:
            return amount[-2];