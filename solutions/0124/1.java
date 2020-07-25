class Solution {
    int res;

    public int maxPathSum(TreeNode root) {
        res = Integer.MIN_VALUE;
        traverse(root);
        return res;
    }

    // return max root path sum
    int traverse(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = traverse(root.left);
        int right = traverse(root.right);
        int maxPathSum = root.val + Math.max(0, left) + Math.max(0, right);
        res = Math.max(res, maxPathSum);
        return root.val + Math.max(0, Math.max(left, right));
    }
}