#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0;
        right=1;
        max_Profit=0;
        profit=0;
        
        while right<len(prices):
            if prices[left]<prices[right]:
                profit=max(max_Profit,prices[right]-prices[left]);
                max_Profit=max(max_Profit,profit);
            else:
                left=right;
                
            right+=1;
        return max_Profit;