class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        result = 0
        start, end = 0, 0
        i = len(s) - 1
        while i >= 0:
            j = i + 1
            dp[i][i] = True
            while j < len(s):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j == i + 1):
                    dp[i][j] = True
                    if j - i + 1 > result:
                        result = j - i + 1
                        start = i
                        end = j
                j += 1
            i -= 1
        return s[start:end + 1]

# class Solution {
#     public String longestPalindrome(String s) {
#         boolean[][] dp = new boolean[s.length()][s.length()];
#         int max = 0;
#         String res = new String();
#         // for this problem, we have to go from the bottom to the top
#         // dp[i][j] relys on dp[i+1][j-1], dp[i+1][j-1] is at the bottom left of dp[i][j]
#         // so to determin dp[i][j], we need to have dp[i+1][j-1] first
#         for ( int i = s.length() - 1; i >= 0; i--) {
#             // we only need half of the matrix table, since dp[i][j] is essentially the same as dp[j][i]
#             for (int j = i; j< s.length(); j++) {
#                 if ( i == j) {
#                     dp[i][j] = true;
#                 } else {
#                     // combine base case 2 and general case into one line
#                     dp[i][j] = (s.charAt(i) == s.charAt(j)) && (dp[i+1][j-1] || j == i+1);
#                 }
                
#                 if (dp[i][j] && (j - i +1 > max)) {
#                     res = s.substring(i, j+1);
#                     max = j - i +1;
#                 }
#             }
#         }
#         return res;
#     }
# }



# Take 2:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # dp[i][i] = True
        # dp[i][j] = True only if s[i] == s[j] and dp[i + 1][j - 1] = True
        # dp[i][i + 1] = True only if s[i] == s[i + 1]
        max_len = 0
        i = len(s) - 1
        start = 0
        end = 0
        while i >= 0:
            dp[i][i] = True
            j = i + 1
            while j <= len(s) - 1:
                if j == i + 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                if dp[i][j] and j - i + 1>= max_len:
                    max_len = j - i + 1
                    start = i
                    end = j
                j += 1
            i -= 1
        return s[start:end + 1]


# Take 3:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, i, j):
            # return the longest parlindrome string length
            left = i
            right = j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if len(s) == 0:
            return ""
        start = 0
        end = 0
        max_len = 0
        for i in range(len(s)):
            len_1 = expand(s, i, i)
            len_2 = expand(s, i, i + 1)
            l = max(len_1, len_2)
            if l > max_len:
                max_len = l
                # This is very important
                start = i - (l - 1) // 2
                end = i + l // 2
        return s[start:end + 1]


# Take 4: DP solution
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        dp[i][j] = s[i,j] is palindrome
        dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        base case: dp[i][i] = true
                dp[i][i + 1] = s[i] == s[i + 1]
        """
        max_len = 1
        start = 0
        end = 0

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1] and 2 > max_len:
                start = i
                end = i + 1


        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 2, len(s)):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
                    end = j

        return s[start:end + 1]

