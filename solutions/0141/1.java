public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            // fast 和 slow 指向同一个结点，说明存在“套圈”
            if (fast == slow) {
                return true;
            }
        }
        // fast 到达链表尾部，则不存在环
        return false;
    }
}