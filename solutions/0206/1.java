class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode cnext = curr.next;
            if (prev == null) {
                curr.next = null;
            } else {
                curr.next = prev;
            }
            prev = curr;
            curr = cnext;
        }
        return prev;
    }
}