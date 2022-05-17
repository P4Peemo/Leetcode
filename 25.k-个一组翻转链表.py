#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode], tail: Optional[ListNode]):
        prev = tail.next
        p = head
        while prev != tail:
            next_one = p.next
            p.next = prev
            prev = p
            p = next_one
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre_head = ListNode(-1)
        pre_head.next = head
        prev = pre_head

        while head:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if tail is None:
                    return pre_head.next
            next_one = tail.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = next_one
            prev = tail
            head = tail.next
        
        return pre_head.next
# @lc code=end

