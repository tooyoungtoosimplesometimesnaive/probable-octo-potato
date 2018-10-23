class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen(left, right, size, current, result): # size is the number of left or right parentheses
            if left == size and right == size:
                result.append(current)
                return
            if left > right and left <= size:
                gen(left, right + 1, size, current + ")", result)
            if left <= size:
                gen(left + 1, right, size, current + "(", result)
        
        result = []
        gen(0, 0, n, "", result)
        return result


