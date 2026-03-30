class MedianFinder:

    def __init__(self):
        # two heaps, large (min heap), small (max heap)
        # should be equal size (heaps)
        self.small, self.large = [], []

    # all heap operations (add/remove) log n
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # library, Python only implements min heaps
        # times -1 makes it a max heap

        # each num in small must be <= than each num in large
        # need to multiply by -1 again to reverse multiplying by -1 maxheap
        if (self.small and self.large and ( -1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small) # need to reverse x -1
            heapq.heappush(self.large, val)

        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small) # need to reverse x -1
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large) 
            heapq.heappush(self.small, -1 * val) # need to reverse x -1
 
    def findMedian(self) -> float:
        # odd num elements
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        # even num elements
        return ((-1 * self.small[0]) + self.large[0]) / 2

        
        