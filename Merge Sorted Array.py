#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        firstPointer=m-1
        secondPointer=m+n-1
        thirdPointer=n-1
        while firstPointer>=0 and thirdPointer>=0:
            if nums2[thirdPointer]>nums1[firstPointer]:
                nums1[secondPointer]=nums2[thirdPointer];
                
                thirdPointer-=1;
            else:
                nums1[secondPointer]=nums1[firstPointer];
                firstPointer-=1;
            secondPointer-=1
        if thirdPointer>=0:
            nums1[:thirdPointer+1]=nums2[:thirdPointer+1];
        