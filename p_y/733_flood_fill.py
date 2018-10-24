class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row = len(image)
        if row == 0:
            return []
        col = len(image[0])
        
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = []
        q.append((sr, sc))
        original_color = image[sr][sc]
        while q:
            top = q.pop(0)
            if top not in visited:
                visited.add(top)
                x, y = top
                image[x][y] = newColor
                
                for dx, dy in directions:
                    if x + dx < row and x + dx >= 0 and y + dy < col and y + dy >= 0 and image[x + dx][y+ dy] == original_color:
                        q.append((x + dx, y + dy))
                
        return image

