class Solution {
    // 用一个类包装递归函数的四个返回值
    class TreeInfo {
        boolean isBST;
        int min;
        int max;
        int sum;

        TreeInfo(boolean isBST, int min, int max, int sum) {
            this.isBST = isBST;
            this.min = min;
            this.max = max;
            this.sum = sum;
        }
    }

    int maxSum; // 全局变量：记录二叉搜索子树的结点之和的最大值

    public int maxSumBST(TreeNode root) {
        maxSum = 0;
        traverse(root);
        return maxSum;
    }

    TreeInfo traverse(TreeNode root) {
        // base case：空子树是二叉搜索树，最小值、最大值不存在，和为 0
        if (root == null) {
            return new TreeInfo(true, Integer.MAX_VALUE, Integer.MIN_VALUE, 0);
        }
        // 递归计算左右子树的子问题
        TreeInfo left = traverse(root.left);
        TreeInfo right = traverse(root.right);
        // 套用公式：计算结点之和
        int sum = root.val + left.sum + right.sum;
        // 套用公式：判断是否是二叉搜索树
        if (left.isBST && right.isBST && left.max < root.val && root.val < right.min) {
            // 当前子树是二叉搜索树的情况
            maxSum = Math.max(maxSum, sum);
            // 套用公式：计算二叉树最小值和最大值
            int min = Math.min(left.min, root.val);
            int max = Math.max(right.max, root.val);
            return new TreeInfo(true, min, max, sum);
        } else {
            // 当前子树不是二叉搜索树的情况
            return new TreeInfo(false, Integer.MAX_VALUE, Integer.MIN_VALUE, sum);
        }
    }
}