class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] not in ['*', '/']:
                stack.append(s[i])
            else:
                stack.append(int(stack.pop()) * int(s[i + 1]))
                i += 1
            i += 1
            
        print("HERE", stack)

        while len(stack) >= 3:
            n1 = int(stack.pop())
            print(n1)
            expr = stack.pop()
            n2 = int(stack.pop())
            print(n2)
            print(len(stack))
            if expr == '+':
                stack.insert(0, n1 + n2)
            else:
                stack.insert(0, n1 - n2)

        return stack[0]


print(Solution().calculate("3+2*2"))