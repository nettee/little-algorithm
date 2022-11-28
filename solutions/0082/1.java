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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            if (curr.next != null && curr.val == curr.next.val) {
                ListNode q = curr;
                while (q != null && q.val == curr.val) {
                    q = q.next;
                }
                if (prev == null) {
                    head = q;
                } else {
                    prev.next = q;
                }
                curr = q;
            } else {
                prev = curr;
                curr = curr.next;
            }
        }
        return head;
    }
}
