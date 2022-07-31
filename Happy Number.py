class Solution:
    def isHappy(self, n: int) -> bool:
        numbers=set();
        while n not in numbers:
            numbers.add(n);
            n=self.SquareOfNumber(n);
            if n==1:
                return True;
        return False;
        
            
            
            
    def SquareOfNumber(self,i):
        output=0;
        while i:
            remainder=i%10;
            output+=(remainder**2);
            i//=10;
        return output;