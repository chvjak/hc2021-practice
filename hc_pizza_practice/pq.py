import heapq as hq
class PQ:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap

    def enque(self, priority, value):
        entry = [-priority, value]
        hq.heappush(self.pq, entry)

    def deque(self):
        priority, value = hq.heappop(self.pq)
        return value 
