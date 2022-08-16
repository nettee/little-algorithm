class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = nullptr;

        while (curr != nullptr) {
            ListNode* cnext = curr->next;
            if (prev == nullptr) {
                curr->next = nullptr;
            } else {
                curr->next = prev;
            }

            prev = curr;
            curr = cnext;
        }
        
        return prev;
    }
};
