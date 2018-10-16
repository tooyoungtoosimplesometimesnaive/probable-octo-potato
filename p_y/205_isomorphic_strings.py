class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t_char_map = {}
        t_s_char_map = {}
        for s_char, t_char in zip(s, t):
            if t_char not in t_s_char_map and s_char not in s_t_char_map: # never been mapped
                t_s_char_map[t_char] = s_char
                s_t_char_map[s_char] = t_char
            elif (s_char in s_t_char_map and s_t_char_map[s_char] != t_char) or (t_char in t_s_char_map and t_s_char_map[t_char] != s_char):
                return False
        return True
