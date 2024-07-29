class Solution:
    def search(self, nums, target):

        def binarySearch(l, r):
            if l > r:
                return -1
            
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid
            
            # mid in left portion
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    return binarySearch(l, mid-1)
                else:
                    return binarySearch(mid+1, r)
            
            # mid in right portion
            else:
                if nums[mid] <= target <= nums[r]:
                    return binarySearch(mid+1, r)
                else:
                    return binarySearch(l, mid-1)

        return binarySearch(0, len(nums) - 1)
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums = [1,3], target = 3))