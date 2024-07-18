class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')': '(',
            '}': "{",
            ']': '['
        }
        stack = []

        for i in range(len(s)):
            if s[i] in map.values():
                stack.append(s[i])
            elif len(stack) != 0 and map.get(s[i]) == stack.pop():
                continue
            else:
                return False

        return len(stack) == 0
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("[[]]{{}()[]}"))