class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        p = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                p.append(c)
            else:
                if c == ')':
                    if len(p) > 0 and p[-1] == '(':
                        p.pop(-1)
                    else:
                        return False
                if c == ']':
                    if len(p) > 0 and p[-1] == '[':
                        p.pop(-1)
                    else:
                        return False
                if c == '}':
                    if len(p) > 0 and p[-1] == '{':
                        p.pop(-1)
                    else:
                        return False
        return len(p) == 0

# Without stack, modify in place:
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        idx = 0
        s = list(s)
        for c in s:
            #print(idx)
            if c == '(' or c == '[' or c == '{':
                s[idx] = c
                idx += 1
            else:
                if c == ')':
                    #print(s[idx])
                    if idx > 0 and s[idx - 1] == '(':
                        idx -= 1
                        #print(idx)
                    else:
                        return False
                if c == ']':
                    if idx > 0 and s[idx - 1] == '[':
                        idx -= 1
                    else:
                        return False
                if c == '}':
                    if idx > 0 and s[idx - 1] == '{':
                        idx -= 1
                    else:
                        return False


        return idx == 0

