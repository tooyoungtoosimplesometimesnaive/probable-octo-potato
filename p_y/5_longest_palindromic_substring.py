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
