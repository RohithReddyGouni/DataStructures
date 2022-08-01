class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0;
        right=len(s)-1;
        while left<right:
            while left < right and not self.isalphaNumeric(s[left]):
                left+=1;
            while left<right and not self.isalphaNumeric(s[right]):
                right-=1;
            if s[left].lower()!=s[right].lower():
                return False;
            left+=1;
            right-=1;
        return True;
        
    
    
    
    def isalphaNumeric(self,letter):
        return (ord('A')<=ord(letter)<=ord('Z') or 
                ord('a')<=ord(letter)<=ord('z') or 
                ord('0')<=ord(letter)<=ord('9'));