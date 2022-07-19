#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        HashSet=set();
        count=0;
        for i in range(len(s)):
            if s[i] not in HashSet:
                HashSet.add(s[i]);
            else:
                HashSet.remove(s[i]);
                count+=2;
        if len(HashSet)>0:
            return count+1;
        else:
            return count;