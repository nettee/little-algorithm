class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target+1]; // 默认初始化为 0
        dp[0] = 1; // 注意 base case
        for (int k = 1; k <= target; k++) {
            for (int n : nums) {
                if (k >= n) {
                    dp[k] += dp[k-n];
                }
            }
        }
        return dp[target];
    }
}