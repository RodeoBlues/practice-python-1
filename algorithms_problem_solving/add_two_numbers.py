"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            return None
        ret = curr = None
        carry = 0
        while l1 is not None or l2 is not None:
            sum = 0
            if l1 is not None:
                sum += l1.val
            if l2 is not None:
                sum += l2.val
            sum += carry
            carry = 0
            if ret is None and curr is None:
                curr = ListNode(sum % 10)
                ret = curr
            else:
                new_node = ListNode(sum % 10)
                curr.next = new_node
                curr = curr.next
            if sum >= 10:
                carry = sum / 10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node
        return ret
