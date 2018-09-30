class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)

        i, j = 0, 0
        while j < len(chars):
            current_char = chars[j]
            count = 0
            while j < len(chars) and current_char == chars[j]:
                j += 1
                count += 1
            
            print("i={}, j={}, current_char={}".format(i, j, current_char))
                
            chars[i] = current_char
            i += 1
            if count != 1:
                k = 0
                while k < len(str(count)):
                    chars[i] = str(count)[k]
                    i += 1
                    k += 1
        return i
