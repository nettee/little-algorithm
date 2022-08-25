public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            // 快慢指针相遇，说明链表存在环
            if (fast == slow) {
                // 此时 slow 指针距离环的起点的距离恰好为 a
                ListNode q = head;
                while (q != slow) {
                    slow = slow.next;
                    q = q.next;
                }
                // slow 和 q 相遇的位置一定是环的起点
                return slow;
            }
        }
        // 链表不存在环，返回 null
        return null;
    }
}
