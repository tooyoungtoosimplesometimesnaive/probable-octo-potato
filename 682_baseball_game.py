class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        total_score = 0
        
        stack = []
        
        for op in ops:
            if op == '+':
                s = stack[-1] + stack[-2]
                stack.append(s)
                total_score += s
            elif op == 'D':
                s = stack[-1] * 2
                stack.append(s)
                total_score += s
            elif op == 'C':
                s = stack.pop()
                total_score -= s
            else:
                s = int(op)
                total_score += s
                stack.append(s)
        
        return total_score

