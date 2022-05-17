#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prehead = ListNode(-1)
        prev = prehead
        former, latter = head, head.next
        if latter is None:
            return former

        while former and latter:
            former, latter = latter, former
            prev.next = former
            latter.next = former.next
            former.next = latter
            prev = latter
            former = former.next.next
            latter = latter.next.next if latter.next is not None else None
    
        return prehead.next
# @lc code=end

