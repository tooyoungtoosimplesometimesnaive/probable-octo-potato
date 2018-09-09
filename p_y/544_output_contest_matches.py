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
