class Solution(object):
    def __init__(self):
        self.prec = {
            '*': 3,
            '/': 3,
            '+': 2,
            '-': 2,
            '(': 1
        }
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.do_calc(self.get_post_fix(s))

    def do_calc(self, post_fix):
        stack = []
        i = 0
        while i < len(post_fix):
            token = post_fix[i]
            if token == '+':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a + b)
            elif token == '-':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b - a)
            elif token == '*':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a * b)
            elif token == '/':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b // a)
            else:
                stack.append(token)
            i+=1
        return stack[0]
        
    def get_post_fix(self, s):
        result = []
        op_stack = []
        i = 0
        while i < len(s):
            num = 0
            is_num = False
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                is_num = True
                num = num * 10 + int(s[i])
                i += 1
            if is_num:
                result.append(num)

            if i >= len(s):
                break
            if s[i] == '(':
                op_stack.append('(')
            elif s[i] == ')':
                while op_stack and op_stack[-1] != '(':
                    result.append(op_stack.pop(-1))
                # remove the '(' from the stack
                op_stack.pop(-1)
            elif s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                while op_stack and self.prec[op_stack[-1]] >= self.prec[s[i]]:
                    result.append(op_stack.pop(-1))
                op_stack.append(s[i])
            i += 1
        while op_stack:
            result.append(op_stack.pop(-1))
        #print(result)
        return result
