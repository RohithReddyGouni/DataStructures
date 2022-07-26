#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[];
        suffix=[0]*len(nums);
        suffix[0]=1;
        prefix=[0]*len(nums);
        prefix[len(nums)-1]=1;
        for i in range(1,len(nums)):
            suffix[i]=suffix[i-1]*nums[i-1];
        for j in range(len(nums)-2,-1,-1):
            prefix[j]=prefix[j+1]*nums[j+1];
        for k in range(len(nums)):
            result.append(suffix[k]*prefix[k]);
        return result;


#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums);
        result[0]=1;
        rs=1;
        for i in range(1,len(nums)):
            rs=rs*nums[i-1];
            result[i]=rs;
        rs=1;
        for i in range(len(nums)-2,-1,-1):
            rs=rs*nums[i+1];
            result[i]=result[i]*rs;
        return result;