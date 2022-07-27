#Time Complexity: O(n2)
#Space Complexity: O(1) or O(n)(If library stores the sorted values)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[];
        nums.sort();
        for index,value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue;
            low=index+1;
            high=len(nums)-1;
            while low < high:
                Sum=value+nums[low]+nums[high];
                if Sum >0:
                    high=high-1;
                elif Sum <0:
                    low=low+1;
                else:
                    result.append([value,nums[low],nums[high]]);
                    low+=1;
                    while nums[low]==nums[low-1] and low<high:
                        low+=1;
        return result;
        
        
        
        
        
        
       