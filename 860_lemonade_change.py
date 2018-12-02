class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {}
        change[5] = 0
        change[10] = 0
        change[20] = 0
        
        for b in bills:
            change[b] += 1
            c = b - 5
            if c > 0:
                if self.get_change(change, c) != 0:
                    return False
        return True
    
    def get_change(self, change, c):
        while c >= 20:
            if change[20] > 0:
                change[20] -= 1
                c -= 20
            else:
                break
        while c >= 10:
            if change[10] > 0:
                change[10] -= 1
                c -= 10
            else:
                break
        while c >= 5:
            if change[5] > 0:
                change[5] -= 1
                c -= 5
            else:
                break
        #print(c)
        return c

