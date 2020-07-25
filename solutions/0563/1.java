class Solution {
    int tilt;

    public int findTilt(TreeNode root) {
        tilt = 0;
        traverse(root);
        return tilt;
    }

    // 返回：结点值之和
    int traverse(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = traverse(root.left);
        int right = traverse(root.right);
        // 计算当前子树的坡度，累加到全局变量
        tilt += Math.abs(left - right);
        return root.val + left + right;
    }
}