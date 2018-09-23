class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        result = ""
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 and j >= 0:
            n1 = int(num1[i])
            n2 = int(num2[j])
            #print("{} {}".format(n1, n2))
            s = (n1 + n2 +carry) % 10
            carry = (n1 + n2 + carry) // 10
            #print(s)
            result += str(s)
            i -= 1
            j -= 1
        #print(result[::-1])
        k = i if i >= 0 else j
        num1 = num1 if i >= 0 else num2
        while k >= 0:
            #print("here")
            n = int(num1[k])
            s = (n + carry) % 10
            carry = (n + carry) // 10
            result += str(s)
            k -= 1
        if carry > 0:
            result += "1"
        return result[::-1]
        
