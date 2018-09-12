class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def get_num(c):
            q, r = divmod(int(c, 16), 17)
            if r > 8: q += 1
            return '{:02x}'.format(q * 17)
        return '#' + get_num(color[1:3]) + get_num(color[3:5]) + get_num(color[5:])
