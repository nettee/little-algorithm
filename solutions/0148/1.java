class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode mid = split(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);
    }

    ListNode split(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = null;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }
        prev.next = null;
        return slow;
    }

    ListNode head;
    ListNode tail;

    ListNode merge(ListNode left, ListNode right) {
        head = null;
        tail = null;
        ListNode q1 = left;
        ListNode q2 = right;
        while (q1 != null || q2 != null) {
            if (q1 == null) {
                append(q2);
                q2 = q2.next;
            } else if (q2 == null) {
                append(q1);
                q1 = q1.next;
            } else if (q1.val < q2.val) {
                append(q1);
                q1 = q1.next;
            } else {
                append(q2);
                q2 = q2.next;
            }
        }
        return head;
    }

    void append(ListNode node) {
        if (head == null) {
            head = node;
            tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
    }
}