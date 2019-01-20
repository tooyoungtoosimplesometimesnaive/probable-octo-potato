class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        next_greater = dict()
        stack = []
        
        i = len(nums2) - 1
        next_greater[nums2[i]] = -1
        stack.append(nums2[i])
        i -= 1
        while i >= 0:
            if nums2[i] > stack[-1]:
                while len(stack) > 0 and nums2[i] > stack[-1]:
                    stack.pop()
                # stack.append(nums2[i])

                next_greater[nums2[i]] = stack[-1] if len(stack) > 0 else -1
                stack.append(nums2[i])

            else:
                next_greater[nums2[i]] = stack[-1]
                stack.append(nums2[i])

            i -= 1
        
        return list(map(lambda i : next_greater[i], nums1))

