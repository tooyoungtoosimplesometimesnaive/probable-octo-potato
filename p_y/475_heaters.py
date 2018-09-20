class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        
        heaters = [float('-inf')] + heaters + [float('inf')]
        ans, i = 0, 0
        for house in houses:
            while heaters[i + 1] < house:
                i += 1
            dis = min(house - heaters[i], heaters[i + 1] - house)
            ans = max(ans, dis)
        return ans
            
         
