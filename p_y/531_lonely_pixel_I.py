class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        row = len(picture)
        col = len(picture[0])
        row_count = [0 for i in range(row)]
        col_count = [0 for i in range(col)]
        
        for i in range(row):
            count = 0
            for j in range(col):
                if picture[i][j] == 'B':
                    count += 1
            row_count[i] = count

        for j in range(col):
            count = 0
            for i in range(row):
                if picture[i][j] == 'B':
                    count += 1
            col_count[j] = count
        
        result = 0
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    result += 1
        return result
