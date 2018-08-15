class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(map(lambda k: "FizzBuzz" if k % 3 == 0 and k % 5 == 0 else "Fizz" if k % 3 == 0 else "Buzz" if k % 5 == 0 else str(k), [x for x in range(1, n + 1)]))

