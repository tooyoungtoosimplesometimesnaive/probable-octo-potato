class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        teams = list(map(str, range(1, n + 1)))
        while n > 1:
            for i in range(n // 2):
                teams[i] = "({},{})".format(teams[i], teams.pop())
            n = n // 2
        
        return teams[0]


# Take 2:
class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.helper(1, 2, 2, n)

    def helper(self, i, j, k, n):
        if k == n:
            return "(" + str(i) + "," + str(j) + ")"

        k = k * 2
        return "(" + self.helper(i, k + 1 - i, k, n) + "," + self.helper(j, k + 1 - j, k, n) + ")"

