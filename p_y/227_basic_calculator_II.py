class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 3 + 2 * 2 + 4 -> 3 2 2 4 -> 3 2 2 * + 4 +
        post_fix = self.to_post_fix(s)
        stack = []
        i = 0
        while i < len(post_fix):
            current = post_fix[i]
            if current == '*':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a * b)
            elif current == '/':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b // a) 
            elif current == '+':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(a + b)
            elif current == '-':
                a = stack.pop(-1)
                b = stack.pop(-1)
                stack.append(b - a)
            else:
                stack.append(post_fix[i])
            i += 1
        
        return stack[0]

    def to_post_fix(self, s):
        op_stack = []
        result = []
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
            
            if s[i] == '*' or s[i] == '/':
                while op_stack and (op_stack[-1] == '*' or op_stack[-1] == '/'):
                    result.append(op_stack.pop(-1))
                op_stack.append(s[i])
            if s[i] == '+' or s[i] == '-':
                while op_stack:
                    result.append(op_stack.pop(-1))
                op_stack.append(s[i])
            
            i += 1

        while op_stack:
            result.append(op_stack.pop(-1))

        return result
