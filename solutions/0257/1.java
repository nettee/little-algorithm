/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        traverse(root, "", result);
        return result;
    }

    private void traverse(TreeNode root, String s, List<String> result) {
        if (root == null) {
            return;
        }
        String ss;
        if (s.isEmpty()) {
            ss = String.valueOf(root.val);
        } else {
            ss = s + "->" + root.val;
        }
        if (root.left == null && root.right == null) {
            result.add(ss);
        }
        traverse(root.left, ss, result);
        traverse(root.right, ss, result);
    }
}
