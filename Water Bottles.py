#Time Complexity: O(logn)
#Space Complexity: O(1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result=numBottles;
        while numBottles>=numExchange:
            Exchange=numBottles//numExchange;
            result+=Exchange;
            numBottles=numBottles%numExchange;
            numBottles+=Exchange;
        return result;