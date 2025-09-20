from collections import deque
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.destMap = dict()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.seen:
            return False

        if len(self.queue) >= self.memoryLimit:
            oldSource, oldDest, oldTs = self.queue.popleft()
            self.seen.remove((oldSource, oldDest, oldTs))
            self.destMap[oldDest].pop(0)

        self.queue.append(packet)
        self.seen.add(packet)
        if destination not in self.destMap:
            self.destMap[destination] = []
        self.destMap[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dest, ts = self.queue.popleft()
        self.seen.remove((src, dest, ts))
        self.destMap[dest].pop(0)
        return [src, dest, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destMap:
            return 0
        
        timestamps = self.destMap[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)