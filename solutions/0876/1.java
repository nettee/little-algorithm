class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            // fast 一次前进两个元素，slow 一次前进一个元素
            fast = fast.next.next;
            slow = slow.next;
        }
        // 链表元素为奇数个时，slow 指向链表的中点
        // 链表元素为偶数个时，slow 指向链表两个中点的右边一个
        return slow;
    }
}