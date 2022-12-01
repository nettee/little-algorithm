/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int sum = 0;
        int d = 0;
        traverse(root, d, sum);
        return sum;
    }

    void traverse(TreeNode* root, int d, int& sum) {
        if (root == nullptr) {
            return;
        }
        int dd = d * 10 + root->val;
        if (root->left == nullptr && root->right == nullptr) {
            sum += dd;
        }
        traverse(root->left, dd, sum);
        traverse(root->right, dd, sum);
    }
};
