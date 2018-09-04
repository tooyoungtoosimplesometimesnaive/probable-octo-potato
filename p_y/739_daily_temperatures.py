class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0 for i in range(len(temperatures))]

        i = len(temperatures) - 1
        while i >= 0:
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if result[j] > 0:
                    j = result[j] + j
                else:
                    j = len(temperatures)

            
            if j < len(temperatures):
                result[i] = j - i
            i -= 1
        return result
        
