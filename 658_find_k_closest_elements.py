class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            # Take the last k elements
            return arr[-k:]
        else:
            # binary search to find the lowest number greater than x
            left = 0
            right = len(arr) - 1
            
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= x:
                    left = mid + 1
                else:
                    right = mid
            
            index = left
            print(index)
            
            low = max(0, index - k - 1)
            high = min(len(arr) - 1, index + k - 1)
            
            while high - low > k - 1:
                # compare the distance
                if x - arr[low] <= arr[high] - x:
                    high -= 1
                else:
                    low += 1
            
            return arr[low:high + 1]

