from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans, vals = "", self.hashmap.get(key, [])

        def binarySearch(l, r, ans):
            if l > r:
                return ans
            
            mid = l + ((r - l) // 2)

            if timestamp <= vals[mid][0]:
                return binarySearch(l, mid-1, vals[mid][1])
            else:
                return binarySearch(mid+1, r, ans)
        
        return binarySearch(0, len(vals) - 1, ans)