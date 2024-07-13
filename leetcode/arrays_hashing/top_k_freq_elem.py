from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        # SHORT solution
        return [c[0] for c in Counter(nums).most_common(k)]

        # # LONG solution
        # dict_count = {}

        # for num in nums:
        #     if num in dict_count:
        #         dict_count[num] += 1
        #     else:
        #         dict_count[num] = 1
        
        # rev_dict_count = {v: k for k, v in dict_count.items()}
        # return [val for val in rev_dict_count.values()][:k]


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1], 1))