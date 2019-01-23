class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        stack = []
        
        count = 0
        for i in range(len(num)):
            if len(stack) == 0:
                stack.append(num[i])
                continue
            while len(stack) != 0 and num[i] < stack[-1] and count < k:
                stack.pop()
                count += 1
            
            stack.append(num[i])

        while count < k:
            stack.pop()
            count += 1

        start_index = 0
        while start_index < len(stack) and stack[start_index] == '0':
            start_index += 1
        
        
        return "0" if start_index == len(stack) else "".join(stack[start_index:])

