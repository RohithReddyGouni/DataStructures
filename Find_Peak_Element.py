#Time Complexity - O(log n)  
# Space Complexity - O(1) 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0;
        low=0;
        high=len(nums)-1;
        while low<=high:
            mid=low+((high-low)//2);
            if mid+1 <len(nums) and nums[mid]<nums[mid+1]:
                low=mid+1;
            elif mid-1 >-1 and nums[mid] < nums[mid-1]:
                high=mid-1
            else:
                return mid;



