class Solution:
    def __init__(self):
        self.scope_stack = []

    """
    Evaluate a valid expression
    """
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        self.scope_stack.append({})
        ans = self.eval_inner(expression)
        self.scope_stack.pop()
        return ans
        
    def eval_inner(self, expr):
        if expr[0] != '(':
            if (expr[0] >= '0' and expr[0] <= '9') or expr[0] == '-':
                return int(expr)
            for i in range(len(self.scope_stack) - 1, -1, -1):
                if expr in self.scope_stack[i]:
                    return int(self.scope_stack[i][expr])
        
        next_index = 6 if expr[:2] == "(m" else 5
        #print("the expr={}, input={}".format(expr, expr[next_index : -1]))
        tokens = self.parse(expr[next_index : -1])
        if expr[:2] == "(a":
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expr[:2] == "(m":
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:
            current_scope = self.scope_stack[-1]
            i = 1
            while i < len(tokens):
                current_scope[tokens[i - 1]] = self.evaluate(tokens[i])
                i += 2
            return self.evaluate(tokens[-1])
        
    
    def parse(self, expr):
        # return a list of str
        result = []
        p_bal = 0 # parenthesis balance
        token_buffer = []
        for token in expr.split(" "):
            for c in token:
                if c == '(':
                    p_bal += 1
                if c == ')':
                    p_bal -= 1
            
            token_buffer.append(token)
            if p_bal == 0:
                result.append(" ".join(token_buffer))
                token_buffer.clear()
        if len(token_buffer) > 0:
            result.append(" ".join(token_buffer))
        #print(result)
        return result
                
