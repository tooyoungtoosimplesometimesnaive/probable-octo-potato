class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for v in range(V):
            # left
            i = K
            while i >= 1 and heights[i - 1] <= heights[i]:
                i -= 1
            
            while i < len(heights) - 1 and heights[i] >= heights[i + 1]:
                i += 1
            
            while i > K and  heights[i - 1] <= heights[i]:
                i -= 1
            
            heights[i] += 1
        
        return heights

# Another one:
class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for v in range(V):
            # left
            index = K
            for i in range(K - 1, -1, -1):
                if heights[i] > heights[index]:
                    break
                elif heights[i] < heights[index]:
                    index = i

            if index != K:
                heights[index] += 1
                continue


            index = K
            for i in range(K + 1, len(heights)):
                if heights[i] > heights[index]:
                    break
                elif heights[i] < heights[index]:
                    index = i

            #this time add anyway
            heights[index] += 1

        return heights

