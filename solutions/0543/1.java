class Solution {
    int diameter;

    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 0;
        traverse(root);
        return diameter;
    }

    // 返回树的深度
    int traverse(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = traverse(root.left); // 左子树的深度
        int right = traverse(root.right); // 右子树的深度
        // 直接访问全局变量
        diameter = Math.max(diameter, left + right);
        return 1 + Math.max(left, right);
    }
}