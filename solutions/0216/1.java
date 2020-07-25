class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        Deque<Integer> current = new ArrayDeque<>();
        List<List<Integer>> res = new ArrayList<>();
        backtrack(k, 1, n, current, res);
        return res;
    }

    // 候选集合：整数 [m..9]
    // 代码调整处：加入参数 k
    void backtrack(int k, int m, int target, Deque<Integer> current, List<List<Integer>> res) {
        if (target < 0) {
            return;
        } else if (target == 0) {
            // 代码调整处：已选集合达到 k 个元素才收集结果
            if (current.size() == k) {
                res.add(new ArrayList<>(current));
            }
            return;
        }
        if (current.size() > k) {
            return;
        }

        // 从候选集合中选择
        for (int i = m; i <= 9; i++) {
            // 选择数字 i
            current.addLast(i);
            // 数字 [m..i) 均失效
            backtrack(k, i+1, target - i, current, res);
            // 撤销选择
            current.removeLast();
        }
    }
}