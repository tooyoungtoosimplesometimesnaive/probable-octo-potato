class Solution:

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        self.row = len(heightMap)
        if self.row == 0:
            return 0
        self.col = len(heightMap[0])
        
        if self.row < 2 or self.col < 2:
            return 0

        pool = []
        visited = [[False for _ in range(self.col)] for _ in range(self.row)]

        self.add_boundary(heightMap, pool, visited)
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        result = 0
        while len(pool) > 0:
            h, i, j = heapq.heappop(pool)

            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if x >= 0 and x < self.row and y >= 0 and y < self.col and not visited[x][y]:
                    visited[x][y] = True
                    result += max(0, h - heightMap[x][y])
                    # This max(h, heightMap[x][y]) is really important
                    heapq.heappush(pool, (max(h, heightMap[x][y]), x, y))
        
        return result

    def add_boundary(self, m, pool, visited):
        for i in range(self.row):
            visited[i][0] = True
            heapq.heappush(pool, (m[i][0], i, 0))
            visited[i][self.col - 1] = True
            heapq.heappush(pool, (m[i][self.col - 1], i, self.col - 1))
        for j in range(1, self.col - 1):
            visited[0][j] = True
            heapq.heappush(pool, (m[0][j], 0, j))
            visited[self.row - 1][j] = True
            heapq.heappush(pool, (m[self.row - 1][j], self.row - 1, j))
            

