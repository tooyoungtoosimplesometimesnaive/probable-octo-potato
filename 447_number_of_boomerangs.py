class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for p1x, p1y in points:
            count_map = collections.defaultdict(int)
            for p2x, p2y in points:
                d = (p1x - p2x) * (p1x - p2x) + (p1y - p2y) * (p1y - p2y)
                if d != 0:
                    count_map[d] += 1
            
            for d, count in count_map.items():
                result += count * (count - 1)
        
        return result

