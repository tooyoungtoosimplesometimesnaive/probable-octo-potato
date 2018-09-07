class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def go_one_dir(maze, start, d):
            # d: direction (1, 0) (0, 1) (-1, 0) (0, -1)
            def blocked(maze, x, y):
                if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
                    return True
                if maze[x][y] == 1:
                    return True
                return False
                
            dx, dy = d
            sx, sy = start
            while not blocked(maze, sx + dx, sy + dy):
                sx += dx
                sy += dy
            return [sx, sy]
        
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def has_path(maze, start, destination, visited):
            if start == destination:
                return True
            for direction in d:
                next_start = go_one_dir(maze, start, direction)
                nsx, nsy = next_start
                if not visited[nsx][nsy]:
                    visited[nsx][nsy] = True
                    if has_path(maze, next_start, destination, visited):
                        return True
            return False
        visited = [[False for i in range(len(maze[0]))] for k in range(len(maze))]
        return has_path(maze, start, destination, visited)
                    
