class Solution:
    def __init__(self):
        self.keyboard = {
            '2': 'abc', '3':'def', '4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(digits, i, current, result):
            if i == len(digits):
                result.append(current)
                return
            for c in self.keyboard[digits[i]]:
                #current.append(c)
                dfs(digits, i + 1, current + c, result)
                #current.pop(-1)
        if len(digits) == 0:
            return []
        result = []
        dfs(digits, 0, '', result)
        return result

