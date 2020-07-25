class Solution {
    public ListNode removeNthFromEnd(ListNode head, int k) {
        // 将 fast 前进 k 个元素
        ListNode fast = head;
        for (int i = 0; i < k; i++) {
            // 这里省略了检测空指针的代码
            fast = fast.next;
        }
        // fast 和 slow 指针间隔 k 个同时前进
        // 这里使用了链表遍历框架，将 slow 指针变成两个指针 curr 和 prev
        ListNode curr = head;
        ListNode prev = null;
        while (fast != null) {
            prev = curr;
            curr = curr.next;
            fast = fast.next;
        }
        if (prev == null) {
            head = curr.next;
        } else {
            prev.next = curr.next;
        }
        return head;
    }
}