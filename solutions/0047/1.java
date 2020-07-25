class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<Integer> current = new ArrayList<>();
        for (int n : nums) {
            current.add(n);
        }
        List<List<Integer>> res = new ArrayList<>();
        backtrack(current, 0, res);
        return res;
    }

    // 已选集合 current[0..m)，候选集合 current[m..N)
    void backtrack(List<Integer> current, int m, List<List<Integer>> res) {
        if (m == current.size()) {
            res.add(new ArrayList<>(current));
            return;
        }

        // 使用 set 辅助判断相等的候选元素是否已经出现过
        Set<Integer> seen = new HashSet<>();
        for (int i = m; i < current.size(); i++) {
            int e = current.get(i);
            if (seen.contains(e)) {
                // 如果已经出现过相等的元素，则不选此元素
                continue;
            }
            seen.add(e);
            Collections.swap(current, m, i);
            backtrack(current, m+1, res);
            Collections.swap(current, m, i);
        }
    }
}