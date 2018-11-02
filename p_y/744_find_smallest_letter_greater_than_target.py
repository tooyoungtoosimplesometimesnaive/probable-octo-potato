class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """            
        l = 0
        r = len(letters) - 1
        while l < r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid
            elif letters[mid] <= target:
                l = mid + 1                

        #print(letters[l])
        if letters[l] > target:
            return letters[l]
        else:
            return letters[0]

