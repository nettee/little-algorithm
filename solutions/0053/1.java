// 解法1：暴力法（会超时）
class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int res = Integer.MIN_VALUE;
        // 穷举各种可能的子数组 nums[i..j]
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                // 计算子数组 nums[i..j] 的和
                int sum = 0;
                for (int k = i; k <= j; k++) {
                    sum += nums[k];
                }
                res = Math.max(res, sum);
            }
        }
        return res;
    }
}