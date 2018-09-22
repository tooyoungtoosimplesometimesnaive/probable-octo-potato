class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # direction:
        # 1 ->
        # 2   / (to left down)
        # 3 down
        # 4 / (to up right)
        def get_dir(row, col, i, j, last_dir):
            if last_dir == 1:
                if i == 0:
                    return 2
                else:
                    return 4
            elif last_dir == 2:
                if i == row - 1 and j == 0:
                    return 1
                elif j == 0:
                    return 3
                elif i == row - 1:
                    return 1
                else:
                    return 2
            elif last_dir == 3:
                if j == 0:
                    return 4
                else:
                    return 2
            elif last_dir == 4:
                if i == 0 and j == col - 1:
                    return 3
                elif i == 0:
                    return 1
                elif j == col - 1:
                    return 3
                else:
                    return 4
        
        if len(matrix) == 0:
            return []
        i,j = 0,0
        row,col = len(matrix), len(matrix[0])
        if col == 1:
            return list(map(lambda x : x[0], matrix))
        if row == 1:
            return matrix[0]

        result = []
        c = 0
        tot = row * col
        direction = 1
        while c < tot:
            # print("{} {}".format(i, j))
            # print(matrix[i][j])
            result.append(matrix[i][j])
            c += 1
            if direction == 1:
                j += 1
            if direction == 2:
                i += 1
                j -= 1
            if direction == 3:
                i += 1
            if direction == 4:
                i -= 1
                j += 1
            direction = get_dir(row, col, i, j, direction)

        return result
