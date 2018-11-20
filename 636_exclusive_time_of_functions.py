class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        result = [0] * n
        func_id, mark, time = logs[0].split(":")
        stack.append(int(func_id))
        prev = int(time)
        i = 1
        while i < len(logs):
            func_id, mark, time = logs[i].split(":")
            if mark == "start":
                if len(stack) != 0:
                    # Not including current time, so there is no + 1
                    result[stack[-1]] += int(time) - prev
                stack.append(int(func_id))
                prev = int(time)
            else:
                result[stack[-1]] += int(time) - prev + 1
                stack.pop(-1)
                prev = int(time) + 1
            
            i += 1
        return result

