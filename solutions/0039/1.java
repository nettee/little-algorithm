class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Deque<Integer> current = new ArrayDeque<>();
        List<List<Integer>> res = new ArrayList<>();
        backtrack(candidates, 0, target, current, res);
        return res;
    }

    // 候选集合 candidates[m..N)
    void backtrack(int[] candidates, int m, int target, Deque<Integer> current, List<List<Integer>> res) {
        if (target < 0) {
            return;
        } else if (target == 0) {
            res.add(new ArrayList<>(current));
            return;
        }

        for (int i = m; i < candidates.length; i++) {
            // 选择数字 candidates[i]
            current.addLast(candidates[i]);
            // 代码调整处：递归调用参数
            // 递归调用传递 i 而不是原先的 i+1
            // 这样 candidates[i] 选完后仍然在候选集合里，后续仍然可以再选
            backtrack(candidates, i, target - candidates[i], current, res);
            // 撤销选择
            current.removeLast();
        }
    }
}