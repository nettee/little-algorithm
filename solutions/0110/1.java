class Solution {
    boolean balanced;

    public boolean isBalanced(TreeNode root) {
        balanced = true;
        traverse(root);
        return balanced;
    }

    // 返回树的高度
    int traverse(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = traverse(root.left);
        int right = traverse(root.right);
        // 判断当前子树是否平衡，修改全局变量
        if (Math.abs(left - right) > 1) {
            balanced = false;
        }
        return 1 + Math.max(left, right);
    }
}