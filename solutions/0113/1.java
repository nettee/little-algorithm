class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        Deque<Integer> path = new ArrayDeque<>();
        traverse(root, sum, path, res);
        return res;
    }

    void traverse(TreeNode root, int sum, Deque<Integer> path, List<List<Integer>> res) {
        if (root == null) {
            return;
        }
        path.addLast(root.val);
        if (root.left == null && root.right == null) {
            if (root.val == sum) {
                res.add(new ArrayList<>(path));
            }
        }
        int target = sum - root.val;
        traverse(root.left, target, path, res);
        traverse(root.right, target, path, res);
        path.removeLast();
    }
}