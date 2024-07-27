class Solution:
    def search(self, nums, target):
        
        # binary serach
        def binarySearch(l, r):
            if l > r:
                return -1
            
            mid = l + ((r - l) // 2) # "(l + r) // 2" might overflow for very large values of l, r

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binarySearch(l, mid-1)
            else:
                return binarySearch(mid+1, r)
        
        return binarySearch(0, len(nums) - 1)
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums = [-1,0,3,5,9,12], target = 2))