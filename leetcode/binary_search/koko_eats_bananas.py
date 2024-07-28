import math


class Solution:
    def minEatingSpeed(self, piles, h):

        def binarySearch(l, r, res):
            if l > r:
                return res
            
            mid = l + ((r - l) // 2)

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / mid)
            
            if totalTime <= h:
                res = mid
                return binarySearch(l, mid-1, res)
            else:
                return binarySearch(mid+1, r, res)
        
        l, r = 1, max(piles)
        res = r
        return binarySearch(l, r, res)

if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed(piles = [3,6,7,11], h = 8))