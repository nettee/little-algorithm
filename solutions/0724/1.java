class Solution {
    public int pivotIndex(int[] nums) {
        // 首先计算所有元素之和 S
        int S = 0;
        for (int n : nums) {
            S += n;
        }

        int A = 0; // A 为前缀和
        // 迭代计算前缀和
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (2 * A + x == S) {
                // 满足公式中的关系，x 是枢纽元素
                return i;
            }
            A += x; // 计算前缀和
        }
        return -1;
    }
}