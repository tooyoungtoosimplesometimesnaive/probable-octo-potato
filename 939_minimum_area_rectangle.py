class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        s = set()
        for point in points:
            s.add(tuple(point))
        
        #print(s)
        ans = float('inf')

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2 and (x1, y2) in s and (x2, y1) in s:
                    #print('h')
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        
        return ans if ans < float('inf') else 0

