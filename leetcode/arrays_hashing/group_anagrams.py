class Solution:
    def groupAnagrams(self, strs):
        dict_anagrams = {}

        for string in strs:
            key = ''.join(sorted(string))
            if key in dict_anagrams:
                dict_anagrams[key].append(string)
            else:
                dict_anagrams[key] = [string]

        return list(dict_anagrams.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["a"]))