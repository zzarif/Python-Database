class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)

        max_length = 0
        for num in numSet:
            # check if num is starting of a sequence
            if num - 1 not in numSet:
                current_length = 1
                # now find the length of this sequence
                while num + current_length in numSet:
                    current_length += 1
                max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))
