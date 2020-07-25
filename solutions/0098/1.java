TreeNode prev; // 全局变量：指向中序遍历的上一个结点
boolean valid;

public boolean isValidBST(TreeNode root) {
    valid = true;
    prev = null;
    traverse(root);
    return valid;
}

void traverse(TreeNode curr) {
    if (curr == null) {
        return;
    }

    traverse(curr.left);

    // 中序遍历的写法，把操作写在两个递归调用中间
    if (prev != null && prev.val >= curr.val) {
        // 如果中序遍历的相邻两个结点大小关系不对，则二叉搜索树不合法
        valid = false;
    }
    // 维护 prev 指针
    prev = curr;

    traverse(curr.right);
}