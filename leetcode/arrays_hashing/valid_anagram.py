from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # # SOLUTION 2
        # if len(s) != len(t):
        #     return False
        # else:
        #     s_char_count = Counter(s)
        #     t_char_count = Counter(t)
        #     return s_char_count == t_char_count
        
    

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    solution = Solution()
    print(solution.isAnagram(s, t))