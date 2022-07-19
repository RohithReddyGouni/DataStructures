#Time Complexity: n(m*mlogm)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap={};
        for word in strs:
            key=''.join(sorted(word))
            if key not in hashMap:
                hashMap[key]=[word];
            else:
                hashMap[key].append(word);
        result=[];
        for Value in hashMap:
            result.append(hashMap[Value]);
        return result;