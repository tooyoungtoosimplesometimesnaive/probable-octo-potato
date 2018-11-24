class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        char_map = collections.defaultdict(int)
        for c in s:
            char_map[c] += 1
        
        odd_char = ''
        for k, v in char_map.items():
            if v % 2 == 1:
                if odd_char != '':
                    return []
                else:
                    odd_char = k
        if odd_char != '':
            char_map[odd_char] -= 1
        
        half_s = []
        for k, v in char_map.items():
            for i in range(v // 2):
                half_s.append(k)

        #print(half_s)
        result = []
        self.generate(half_s, result, 0, odd_char)
        return result
    
    def generate(self, s, result, i, odd_char):
        if i >= len(s):
            result.append("".join(s + [odd_char] + s[::-1]))
            return
        dedup_set = set()
        for j in range(i, len(s)):
            if s[j] not in dedup_set:
                dedup_set.add(s[j])
                s[j], s[i] = s[i], s[j]
                self.generate(s, result, i + 1, odd_char)
                s[j], s[i] = s[i], s[j]

