/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        ListNode* left_tail = nullptr;
        ListNode* mid_head = nullptr;
        ListNode* mid_tail = nullptr;
        ListNode* right_head = nullptr;

        int pos = 1;
        while (curr != nullptr) {
            ListNode* next = curr->next;
            if (pos == left) {
                left_tail = prev;
                mid_head = curr;
            }
            if (pos >= left && pos <= right) {
                curr->next = prev;
            }
            if (pos == right) {
                if (left_tail == nullptr) {
                    head = curr;
                } else {
                    left_tail->next = curr;
                }
                mid_head->next = next;
            }

            prev = curr;
            curr = next;
            pos++;
        }
        return head;
    }
};
