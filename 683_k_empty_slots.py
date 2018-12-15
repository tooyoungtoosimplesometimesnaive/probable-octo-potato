class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0 for _ in range(len(flowers))]
        for i in range(len(flowers)):
            days[flowers[i] - 1] = i + 1
        
        ans = float('inf')
        
        left = 0
        right = k + 1
        i = 1
        while right < len(days):
            if days[i] > days[left] and days[i] > days[right]:
                i += 1
                continue
                
            if i == right:
                ans = min(ans, max(days[left], days[right]))

            left = i
            right = i + k + 1
            i += 1
        
        return ans if ans < float('inf') else -1

