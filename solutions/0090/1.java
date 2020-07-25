class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        // 对元素排序，保证相等的元素相邻
        Arrays.sort(nums);
        Deque<Integer> current = new ArrayDeque<>(nums.length);
        List<List<Integer>> res = new ArrayList<>();
        backtrack(nums, 0, current, res);
        return res;
    }

    // 候选集合: nums[k..N)
    void backtrack(int[] nums, int k, Deque<Integer> current, List<List<Integer>> res) {
        if (k == nums.length) {
            res.add(new ArrayList<>(current));
            return;
        }

        // 选择 nums[k]
        current.addLast(nums[k]);
        backtrack(nums, k+1, current, res);
        current.removeLast();

        // 不选择 nums[k]
        // 将后续和 nums[k] 相等的元素 nums[k..j) 都从候选集合中删除
        int j = k;
        while (j < nums.length && nums[j] == nums[k]) {
            j++;
        }
        backtrack(nums, j, current, res);
    }
}