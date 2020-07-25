class Solution {
    public int subarraySum(int[] nums, int k) {
        // 前缀和 -> 该前缀和（的值）出现的次数
        Map<Integer, Integer> presum = new HashMap<>();
        // base case，前缀和 0 出现 1 次
        presum.put(0, 1);

        int sum = 0; // 前缀和
        int res = 0;
        for (int n : nums) {
            sum += n; // 计算前缀和
            // 查找有多少个 sum[i] 等于 sum[j] - k
            if (presum.containsKey(sum - k)) {
                res += presum.get(sum - k);
            }
            // 更新 sum[j] 的个数
            if (presum.containsKey(sum)) {
                presum.put(sum, presum.get(sum) + 1);
            } else {
                presum.put(sum, 1);
            }
        }
        return res;
    }
}