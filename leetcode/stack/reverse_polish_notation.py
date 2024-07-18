class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                # NOTE: (b // a) will fuck up for negative nums
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack.pop()
    


if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))