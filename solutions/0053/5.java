// 解法5：贪心法
class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0; // 计算当前的部分子数组和
        int res = Integer.MIN_VALUE;
        for (int n : nums) {
            // 如果部分和小于零，直接舍弃，从零开始重新累加
            if (sum < 0) {
                sum = 0;
            }
            sum += n; // 加上当前元素
            res = Math.max(res, sum);
        }
        return res;
    }
}