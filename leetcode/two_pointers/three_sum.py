class Solution:
    def threeSum(self, nums):
        res = []
        target = 0
        nums.sort() # sort list -> O(n * log n)

        # do two_sum for each element
        for i in range(len(nums)):

            # ignore case if it's the same element as before
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # start two_sum for two elements
            l, r = i + 1, len(nums) - 1
            while l < r:
                # case: sum too big
                if nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                # case: sum too small
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                # else match found
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # ignore case if it's the same element as before (from left side)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # no need to do ignore case for right element (r -= 1)
                    # it will taken care of by parent conditions

        return res
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([0,0,0]))
        