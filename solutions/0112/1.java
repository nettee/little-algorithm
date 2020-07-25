class Solution {
    boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        if (root.left == null && root.right == null) {
            return root.val == sum;
        }
        int target = sum - root.val;
        return hasPathSum(root.left, target)
            || hasPathSum(root.right, target);
    }
}