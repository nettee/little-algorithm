class NumArray {

    private int[] preSum;

    // 预处理阶段
    public NumArray(int[] nums) {
        int n = nums.length;
        // 计算前缀和数组
        preSum = new int[n+1];
        preSum[0] = 0;
        for (int i = 0; i < n; i++) {
            preSum[i+1] = preSum[i] + nums[i];
        }
    }

    public int sumRange(int i, int j) {
        return preSum[j+1] - preSum[i];
    }
}