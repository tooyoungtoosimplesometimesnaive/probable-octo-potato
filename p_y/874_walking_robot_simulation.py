class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # print(map(lambda o : str(o[0]) + " " + str(o[1]), obstacles))
        s = set(map(lambda o : str(o[0]) + " " + str(o[1]), obstacles))
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        x = 0
        y = 0
        result = 0
        for c in commands:
            if c == -1:
                d += 1
                if d >= 4:
                    d = 0
            elif c == -2:
                d -= 1
                if d <= -1:
                    d = 3
            else:
                
                while c > 0 and str(x + direction[d][0]) + " " + str(y + direction[d][1]) not in s:
                    x += direction[d][0]
                    y += direction[d][1]
                    c -= 1
            result = max(result, x * x + y * y)
        return result

