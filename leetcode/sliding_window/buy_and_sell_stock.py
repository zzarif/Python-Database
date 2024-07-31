class Solution:
    def maxProfit(self, prices) -> int:
        
        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
                
        return res
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(prices=[5,1,5,6,7,1,10]))