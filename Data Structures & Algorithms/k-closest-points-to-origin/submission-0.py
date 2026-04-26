class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(x**2+y**2)
            heapq.heappush(heap, (-distance,point))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x[1] for x in heap]
        