class Solution {
    int res; // 全局变量：记录最长之字形路径的长度

    public int longestZigZag(TreeNode root) {
        res = 0;
        traverse(root);
        return res - 1;
    }

    // 返回两个值
    // 返回值 0: 最长左之根路径的长度
    // 返回值 1: 最长右之根路径的长度
    int[] traverse(TreeNode root) {
        // base case：空子树的左之、右之路径长度为 0
        if (root == null) {
            return new int[]{0, 0};
        }
        // 递归计算左右子树的子问题
        int[] left = traverse(root.left);
        int[] right = traverse(root.right);
        // 套用公式
        int leftzz = 1 + left[1];
        int rightzz = 1 + right[0];
        // 更新全局变量（主要子问题）
        res = Math.max(res, leftzz);
        res = Math.max(res, rightzz);
        // 返回值（两个辅助子问题）
        return new int[]{leftzz, rightzz};
    }
}