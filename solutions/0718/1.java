class Solution {
    public int findLength(int[] s, int[] t) {
        // 子问题：
        // f(i, j) = s[0..i) 和 t[0..j) 中以 s[i-1] 和 t[j-1] 结尾的最长公共子数组
        // 原问题 = max{ f(i, j) }, 0 <= i <= m, 0 <= j <= n

        // f(0, *) = 0
        // f(*, 0) = 0
        // f(i, j) = max:
        //           f(i-1, j-1) + 1, if s[i-1] == t[j-1]
        //           0              , if s[i-1] != t[j-1]

        int m = s.length;
        int n = t.length;
        int[][] dp = new int[m+1][n+1];

        int res = 0;
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else {
                    if (s[i-1] == t[j-1]) {
                        dp[i][j] = dp[i-1][j-1] + 1;
                    } else {
                        dp[i][j] = 0;
                    }
                }
                res = Math.max(res, dp[i][j]);
            }
        }
        return res;
    }
}