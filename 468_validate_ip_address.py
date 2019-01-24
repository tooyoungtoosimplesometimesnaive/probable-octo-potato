class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.check_ipv4(IP):
            return "IPv4"
        elif self.check_ipv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def check_ipv4(self, ip):
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for p in parts:
            if not self.check_int(p):
                return False
            if len(p) == 0 or int(p) >= 256 or int(p) < 0:
                return False
            if p[0] == '0' and len(p) > 1:
                return False
        return True
    
    
    def check_ipv6(self, ip):
        parts = ip.split(":")
        if len(parts) != 8:
            return False
        for p in parts:
            if len(p) == 0 or len(p) > 4:
                return False
            if not self.check_hex(p):
                return False
        return True
    
    
    def check_int(self, s):
        for c in s:
            if ord(c) < ord('0') or ord(c) > ord('9'):
                return False
        return True
    
    def check_hex(self, s):
        def hex(c):
            return (ord(c) >= ord('0') and ord(c) <= ord('9')) or \
                    (ord(c) >= ord('a') and ord(c) <= ord('f')) or \
                    (ord(c) >= ord('A') and ord(c) <= ord('F'))
        for char in s:
            if not hex(char):
                return False
        return True

