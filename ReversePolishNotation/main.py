"""
Solution is true but runtime 68ms. Second solution's runtime is 57ms.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        opp=["+","-","*","/"] 
        for i in tokens:
            if i not in opp:
                stack.append(int(i))
            else:
                res=0
                num1=stack.pop()
                num2=stack.pop()
                if i=="+":
                    res+=num2+num1
                elif i=="*":
                    res+=num2*num1
                elif i=="-":
                    res+=num2-num1
                elif i=="/":
                    res = int(num2 / num1) if num2 * num1 >= 0 else -(-num2 // num1)
                stack.append(res)
        return stack[-1]

"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            else: stack.append(int(char))

        return stack[0]    
    
tokens = ["4", "-2", "/", "2", "-3", "-", "-"]
sol = Solution()
output = sol.evalRPN(tokens)
print(output)  # Expected output: -7