class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3: return []
        factors = []

        def all_combinations(n, k, factors, current_factors):
            i = k
            while i * i <= n:
                if n % i == 0:
                    factors.append(current_factors + [i, n // i])
                    all_combinations(n // i, i, factors, current_factors + [i])
                i += 1

        all_combinations(n, 2, factors, [])

        return factors
            
