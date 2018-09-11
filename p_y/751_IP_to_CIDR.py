class Solution:
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        def ip_to_num(ip):
            a = list(map(int, ip.split(".")))
            ans = 0
            for i in a:
                ans = ans * 256 + i
            return ans
        def num_to_ip(num):
            return '.'.join(str((num >> i) % 256) for i in [24, 16, 8, 0])
        
        result = []
        start = ip_to_num(ip)
        while n > 0:
            mask = max(33 - (start & -start).bit_length(), 33 - n.bit_length())
            result.append( num_to_ip(start) + "/" + str(mask) )
            start = start + (1 << (32 - mask))
            n -= (1 << (32 - mask))
        return result
