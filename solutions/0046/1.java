class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> current = new ArrayList<>();
        for (int n : nums) {
            current.add(n);
        }
        List<List<Integer>> res = new ArrayList<>();
        backtrack(current, 0, res);
        return res;
    }

    // current[0..k) 是已选集合， current[k..N) 是候选集合
    void backtrack(List<Integer> current, int k, List<List<Integer>> res) {
        if (k == current.size()) {
            res.add(new ArrayList<>(current));
            return;
        }
        // 从候选集合中选择
        for (int i = k; i < current.size(); i++) {
            // 选择数字 current[i]
            Collections.swap(current, k, i);
            // 将 k 加一
            backtrack(current, k+1, res);
            // 撤销选择
            Collections.swap(current, k, i);
        }
    }
}