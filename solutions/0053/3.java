// 解法3：分治法
class Solution {
    public int maxSubArray(int[] nums) {
        return maxSubArray(nums, 0, nums.length - 1);
    }

    // 计算 nums[lo..hi] 的最大子数组和
    // lo 表示 low，hi 表示 high
    private int maxSubArray(int[] nums, int lo, int hi) {
        if (hi < lo) {
            return Integer.MIN_VALUE;
        } else if (hi == lo) {
            return nums[lo];
        }

        int mid = lo + (hi - lo) / 2;
        int max_left = maxSubArray(nums, lo, mid);
        int max_right = maxSubArray(nums, mid+1, hi);
        int max_mid = maxMidSubArray(nums, lo, mid, hi);
        return Math.max(max_left, Math.max(max_mid, max_right));
    }

    private int maxMidSubArray(int[] nums, int lo, int mid, int hi) {
        int max_mid_left = 0;
        if (mid >= lo) {
            max_mid_left = nums[mid];
            int sum = 0;
            for (int i = mid; i >= lo; i--) {
                sum += nums[i];
                max_mid_left = Math.max(max_mid_left, sum);
            }
        }
        int max_mid_right = 0;
        if (mid + 1 <= hi) {
            max_mid_right = nums[mid+1];
            int sum = 0;
            for (int i = mid + 1; i <= hi; i++) {
                sum += nums[i];
                max_mid_right = Math.max(max_mid_right, sum);
            }
        }
        return max_mid_left + max_mid_right;
    }
}