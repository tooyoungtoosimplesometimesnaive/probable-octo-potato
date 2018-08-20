class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        a = "".join(S.split("-"))
        # print(a)
        res = ""
        counter = 0
        len_counter = 0
        for i in a[::-1]:
            counter += 1
            len_counter += 1
            if i >= 'a' and i <= 'z':
                res += i.upper()
            else:
                res += i
            if counter == K:
                counter = 0
                if len_counter != len(a):
                    res += "-"
        
        return res[::-1]

