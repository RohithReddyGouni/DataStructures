class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones];
        heapq.heapify(stones);
        while len(stones)>1:
            firstMax=heapq.heappop(stones);
            secondMax=heapq.heappop(stones);
            firstMax=abs(firstMax);
            secondMax=abs(secondMax);
            if secondMax<firstMax:
                heapq.heappush(stones,secondMax-firstMax);
        stones.append(0);
        return abs(stones[0]);