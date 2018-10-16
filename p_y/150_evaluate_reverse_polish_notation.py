iclass Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def eval_expr(a, b, op): # a, b, op are all str
            
            if op == '/':# be aware of python // operator on negative numbers
                return str(int(int(a) / int(b)))
            else:
                #print(a+op+b)
                return str(eval(a + op + b))
        stack = []
        for t in tokens:
            if t == '*' or t == '+' or t == '-' or t == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                # Pay attention to n1 and n2 order
                stack.append(eval_expr(n2, n1, t))
            else:
                stack.append(t)
        return int(stack.pop())

