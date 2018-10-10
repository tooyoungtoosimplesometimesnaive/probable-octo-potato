class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def transform(S, start, current, results):
            if start >= len(S):
                results.append(current)
                return

            if S[start] >= '0' and S[start] <='9':
                transform(S, start + 1, current + S[start], results)
            else:
                transform(S, start + 1, current + S[start].lower(), results)
                transform(S, start + 1, current + S[start].upper(), results)
        results = []
        transform(S, 0, "", results)
        return results
