class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        r = length
        
        while r < len(s2):
            if sorted(s2[r-length:r]) == sorted(s1):
                return True
            r += 1

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion(s1="ab", s2="eidbaooo"))
