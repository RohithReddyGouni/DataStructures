class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Map1=Counter(nums1);
        HashSet=set();
        for i in range(len(nums2)):
            if nums2[i] in Map1:
                HashSet.add(nums2[i]);
        return HashSet;
            
        
            
        
        