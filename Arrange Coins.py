class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0;
        elements=1;
        while n>0:
            n=n-elements;
            elements+=1;
            if n>=0:
                count+=1;
        return count;