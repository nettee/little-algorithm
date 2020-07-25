class Solution {
    public int coinChange(int[] coins, int amount) {
        // 子问题：
        // f(k) = 凑出金额 k 的最小硬币数

        // f(k) = min{ 1 + f(k - c) }
        // f(0) = 0
        int[] dp = new int[amount+1];
        Arrays.fill(dp, amount + 1); // DP 数组初始化为正无穷大
        dp[0] = 0;
        for (int k = 1; k <= amount; k++) {
            for (int c : coins) {
                if (k >= c) {
                    dp[k] = Math.min(dp[k], 1 + dp[k-c]);
                }
            }
        }
        // 如果 dp[amount] > amount，认为是无效元素。
        if (dp[amount] > amount) {
            return -1;
        } else {
            return dp[amount];
        }
    }
}