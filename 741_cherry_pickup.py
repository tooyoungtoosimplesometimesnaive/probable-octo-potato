# TLE with recursion + memorization
class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        # -2 meaning never visited before
        self.m = [[[-2 for _ in range(N)] for _ in range(N)] for _ in range(N)]
        a = self.dp(grid, N - 1, N - 1, N - 1)
        return max(0, a)

    def dp(self, grid, x1, y1, x2):
        y2 = x1 + y1 - x2
        
        if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
            return -1
        
        if grid[x1][y1] < 0 or grid[x2][y2] < 0:
            return -1
        
        if x1 == 0 and y1 == 0:
            print('here')
            return grid[x1][y1]
        
        if self.m[x1][y1][x2] != -2:
            return self.m[x1][y1][x2]
        
        ans = max(self.dp(grid, x1 - 1, y1, x2), self.dp(grid, x1, y1 - 1, x2), self.dp(grid, x1 - 1, y1, x2 - 1), self.dp(grid, x1, y1 - 1, x2 - 1))
        if ans < 0:
            return -1

        ans += grid[x1][y1]
        if x1 != x2:
            ans += grid[x2][y2]
        
        self.m[x1][y1][x2] = ans
        return ans
        
        
# A working DP solution, slightly different definition:
class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        self.m = [[[-1 for _ in range(N + N)] for _ in range(N)] for _ in range(N)]
        self.m[0][0][0] = grid[0][0]
        for step in range(1, N + N - 1):
            start = 0 if step <= N - 1 else step - (N - 1)
            end = step if step <= N - 1 else N - 1
            for i in range(start, end + 1):
                for j in range(i, end + 1):

                    x1 = i
                    y1 = step - i
                    x2 = j
                    y2 = step - j

                    #print(x1, y1, x2, y2)

                    if x1 >= N or y1 >= N or x2 >= N or y2 >= N:
                        #print('out of bound')
                        continue

                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        #print('can not go')
                        #self.m
                        continue

                    a = max(self.m[x1][x2][step - 1], self.m[x1 - 1][x2][step - 1], \
                                           self.m[x1][x2 - 1][step - 1], self.m[x1 - 1][x2 - 1][step - 1])

                    #print('a is ', a)
                    if a < 0:
                        continue

                    a += grid[x1][y1]
                    if x1 != x2:
                        a += grid[x2][y2]

                    self.m[x1][x2][step] = a

        #print(self.m)
        return max(0, self.m[N - 1][N - 1][N + N - 2])


