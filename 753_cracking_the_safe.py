class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total_number = k ** n
        result = ["0" for _ in range(n)]
        #print(result)
        
        visited = set()
        
        visited.add("".join(result))
        
        self.crack(result, visited, total_number, n, k)
        
        return "".join(result)
    
    def crack(self, result, visited, total_number, n, k):
        if len(visited) == total_number:
            return True
        
        last_n = result[-(n - 1):] if n != 1 else []
        for i in range(k):
            c = chr(ord('0') + i)
            last_n.append(c)
            str_last_n = "".join(last_n)
            if str_last_n not in visited:
                visited.add(str_last_n)
                result.append(c)
                if self.crack(result, visited, total_number, n, k):
                    return True
                visited.remove(str_last_n)
                result.pop()
        return False

