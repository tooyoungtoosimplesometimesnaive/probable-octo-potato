class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return len(s)
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        #print(dp)
        # dp[i][i] = 1
        # dp[i][j] = 2 + dp[i+1][j-1] if s[i] == s[j]
        #     else = max(dp[i+1][j], dp[i][j-1])
        i = len(s) - 1
        while i >= 0:
            dp[i][i] = 1
            j = i + 1
            while j < len(s):
                if s[i] == s[j]:
                    #print(dp[i + 1][j - 1])
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                
                j += 1
            i -= 1
            #print(dp)
        return dp[0][len(s) - 1]

                 
# public class Solution {
#     public int longestPalindromeSubseq(String s) {
#         int[][] dp = new int[s.length()][s.length()];
#         for (int i = s.length() - 1; i >= 0; i--) {
#             dp[i][i] = 1;
#             for (int j = i+1; j < s.length(); j++) {
#                 if (s.charAt(i) == s.charAt(j)) {
#                     dp[i][j] = dp[i+1][j-1] + 2;
#                 } else {
#                     dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
#                 }
#             }
#         }
#         return dp[0][s.length()-1];
#     }
# }



# Take 2: DP solution:
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        dp[i][j] : longest palindrome subseq from s[i] to s[j]
        dp[i][j] =
            if s[i] == s[j]:
                dp[i + 1][j - 1] + 2
            else:
                max(dp[i + 1][j], dp[i][j - 1])
        """
        if s == s[::-1]: return len(s)

        dp = [[1 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s) - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1

        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 2, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]

