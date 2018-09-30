class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)
        i, j = 0, 0
        count = 0
        while j < len(chars):
            if chars[i] != chars[j] or j == len(chars) - 1:
                #print(count)
                count = count if j != len(chars) - 1 else count + 1
                if count == 1:
                    i += 1
                    count = 0
                    chars[i] = chars[j]
                    continue
                k = 0
                count_str = str(count)
                while k < len(count_str):
                    i += 1
                    print("i = {}. k = {}".format(i, k))
                    chars[i] = count_str[k]
                    k += 1
                i += 1
                if j == len(chars) - 1:
                    break
                chars[i] = chars[j]
                count = 0
                
            else:
                j += 1
                count += 1

            
        return i
