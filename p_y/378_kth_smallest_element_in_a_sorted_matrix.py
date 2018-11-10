class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        if k == 0:
            return 0
        visited = [[False for _ in range(col)] for _ in range(row)]
        visited[0][0] = True
        pool = [(matrix[0][0], 0, 0)]
        heapq.heapify(pool)
        count = 0
        result = 0
        while pool:
            top = heapq.heappop(pool)
            val = top[0]
            i = top[1]
            j = top[2]
            result = val
            count += 1
            if count == k:
                return result
            if j + 1 < col and not visited[i][j + 1]:
                heapq.heappush(pool, (matrix[i][j + 1], i, j + 1))
                visited[i][j + 1] = True
            if i + 1 < row and not visited[i + 1][j]:
                heapq.heappush(pool, (matrix[i + 1][j], i + 1, j))
                visited[i + 1][j] = True
        return -1
            
