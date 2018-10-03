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
