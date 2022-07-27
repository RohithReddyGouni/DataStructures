#Time Complexity: O(n)
#Space Complexity: O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentProduct=1;
        maxProduct=-1000000000;
        for i in nums:
            currentProduct*=i;
            
            if currentProduct>maxProduct:
                maxProduct=currentProduct;
            if currentProduct==0:
                currentProduct=1;
    
        currentProduct=1;
        for i in nums[::-1]:
            currentProduct*=i;
            if currentProduct>maxProduct:
                maxProduct=currentProduct;
            if currentProduct==0:
                currentProduct=1;
        return maxProduct;
        