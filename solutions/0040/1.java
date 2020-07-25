class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
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
        }

        for (int i = m; i < candidates.length; i++) {
            // 代码调整处：候选集合遍历
            if (i > m && candidates[i] == candidates[i-1]) {
                // 如果 candidates[i] 与前一个元素相等，说明不是相等元素中的第一个，跳过。
                continue;
            }
            // 选择数字 candidates[i]
            current.addLast(candidates[i]);
            // 元素 candidates[m..i) 均失效
            backtrack(candidates, i+1, target - candidates[i], current, res);
            // 撤销选择
            current.removeLast();
        }
    }
}