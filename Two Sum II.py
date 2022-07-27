#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0;
        high=len(numbers)-1;
        while low<=high:
            sum=numbers[low]+numbers[high];
            if sum==target:
                return low+1,high+1;
            else:
                if sum>target:
                    high=high-1;
                else:
                    low=low+1;