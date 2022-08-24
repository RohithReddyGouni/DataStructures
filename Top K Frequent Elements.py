class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map={}
        length=len(nums)
        Heap=[]
        for i in range(length):
            if nums[i] not in Map:
                Map[nums[i]]=1
            else:
                Map[nums[i]]+=1
        
        for key,values in Map.items():
            heappush(Heap,(values,key))
            if len(Heap)>k:
                heappop(Heap)
                  
        result=[]
         

        for i in range(len(Heap)):
            result.append(Heap[i][1])
        
        return result;