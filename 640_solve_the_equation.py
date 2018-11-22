class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        
        # Move all x to the lhs, and all numbers to the rhs
        lhs = 0
        rhs = 0
        for item in self.break_equation(left):
            if item.find('x') >= 0:
                lhs += int(self.coefficient(item))
            else:
                rhs -= int(item)
        for item in self.break_equation(right):
            if item.find('x') >= 0:
                lhs -= int(self.coefficient(item))
            else:
                rhs += int(item)
        
        if lhs == 0:
            if rhs == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        return "x=" + str(rhs // lhs)
            

    def coefficient(self, item):
        if len(item) > 1 and item[-2] <= '9' and item[-2] >= '0':
            return item.replace('x', "")
        return item.replace('x', "1")

    def break_equation(self, equation):
        result = []
        i = 0
        r = ""
        while i < len(equation):
            if equation[i] == '+' or equation[i] == '-':
                if len(r) > 0:
                    result.append(r)
                r = equation[i]
            else:
                r += equation[i]
            i += 1
        result.append(r)
        return result

