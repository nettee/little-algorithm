class Solution {
    public int change(int amount, int[] coins) {
        int m = coins.length;
        int[][] dp = new int[m+1][amount+1];

        for (int i = 0; i <= m; i++) {
            for (int k = 0; k <= amount; k++) {
                if (k == 0) {
                    dp[i][k] = 1; // base case
                } else if (i == 0) {
                    dp[i][k] = 0; // base case
                } else {
                    dp[i][k] = dp[i-1][k];
                    if (k >= coins[i-1]) {
                        dp[i][k] += dp[i][k-coins[i-1]];
                    }
                }
            }
        }
        return dp[m][amount];
    }
}