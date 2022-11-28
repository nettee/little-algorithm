/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) {
            return null;
        }
        int n = len(head);
        k = k % n;
        if (k == 0) {
            return head;
        }
        ListNode fast = head;
        ListNode slow = head;
        ListNode fprev = null;
        ListNode sprev = null;
        for (int i = 0; i < k; i++) {
            fast = fast.next;
        }
        while (fast != null) {
            fprev = fast;
            fast = fast.next;
            sprev = slow;
            slow = slow.next;
        }
        sprev.next = null;
        fprev.next = head;
        return slow;
    }

    private int len(ListNode head) {
        int n = 0;
        for (ListNode q = head; q != null; q = q.next) {
            n++;
        }
        return n;
    }
}
