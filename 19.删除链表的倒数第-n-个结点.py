#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev_head = ListNode(0, head)
        first = second = prev_head
        while n > 0:
            second = second.next
            n -= 1
        while second.next:
            first = first.next
            second = second.next
        to_remove = first.next
        next_to_remove = to_remove.next
        first.next = next_to_remove
        return prev_head.next
# @lc code=end

