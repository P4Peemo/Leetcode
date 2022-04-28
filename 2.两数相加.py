#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = None
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            digitSum = val1 + val2 + carry

            if not head:
                head = tail = ListNode(digitSum % 10)
            else:
                tail.next = ListNode(digitSum % 10)
                tail = tail.next
            
            carry = digitSum // 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            tail.next = ListNode(carry)

        return head
# @lc code=end

