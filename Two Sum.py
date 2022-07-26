#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map={};
        res=[]
        for i in range(len(nums)):
            result=target-nums[i];
            if result not in Map:
                Map[nums[i]]=i;
            else:
                res.append(i);
                res.append(Map[result]);
        return res;
                
                
        