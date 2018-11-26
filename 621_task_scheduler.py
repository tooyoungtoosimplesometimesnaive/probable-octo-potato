class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        array = [0] * 26
        for task in tasks:
            array[ord(task) - ord('A')] += 1
        
        array = sorted(array)
        
        max_val = array[-1] - 1
        idle_slots = max_val * n
        for i in range(24, -1, -1):
            if array[i] == 0:
                break
            
            idle_slots -= min(array[i], max_val)
        
        
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
    

