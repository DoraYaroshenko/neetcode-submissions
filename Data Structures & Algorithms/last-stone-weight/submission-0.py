class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x*-1 for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1!=stone2:
                max_stone = max(stone1,stone2)
                min_stone=min(stone1,stone2)
                heapq.heappush(stones,min_stone-max_stone)
        if len(stones)==0:
            return 0
        return -stones[0]