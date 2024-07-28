class Solution:
    def findMin(self, nums):

        def binarySearch(l, r, res):
            if l > r:
                return res
            
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])

            if nums[l] <= nums[mid]:
                return binarySearch(mid+1, r, res)
            else:
                return binarySearch(l, mid-1, res)

        l, r = 0, len(nums) - 1
        res = float("inf")
        return binarySearch(l, r, res)
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin(nums = [4,5,6,7,0,1,2]))