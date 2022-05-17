#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        concat_prehead = ListNode()
        curr_node = concat_prehead
        while list1 and list2:
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        if not list1:
            curr_node.next = list2
        if not list2:
            curr_node.next = list1
        return concat_prehead.next

    def merge(self, lists: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        if left > right:
            return None
        mid = (left + right) // 2
        l_part = self.merge(lists, left, mid)
        r_part = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l_part, r_part)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists) - 1)
        
# @lc code=end

