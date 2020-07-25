// 解法4：动态规划
class Solution {
    public int maxSubArray(int[] nums) {
        // 子问题：
        // f(k) = nums[0..k) 中以 nums[k-1] 结尾的最大子数组和
        // 原问题 = max{ f(k) }, 0 <= k <= N

        // f(0) = 0
        // f(k) = max{ f(k-1), 0 } + nums[k-1]

        int N = nums.length;
        int[] dp = new int[N+1];
        dp[0] = 0;

        int res = Integer.MIN_VALUE;
        for (int k = 1; k <= N; k++) {
            dp[k] = Math.max(dp[k-1], 0) + nums[k-1];
            res = Math.max(res, dp[k]);
        }
        return res;
    }
}