__author__ = 'chi'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        head = ListNode((l1.val+l2.val)%10)
        flag = (l1.val+l2.val) >= 10
        movehead = head
        p1 = l1.next
        p2 = l2.next

        while p1 != None and p2 != None:
            tmp = ListNode((p1.val+p2.val+flag)%10)
            flag = (p1.val+p2.val+flag) >= 10
            movehead.next = tmp
            movehead = movehead.next
            p1 = p1.next
            p2 = p2.next

        if p1 == None and p2 != None:
            while p2:
                tmp = ListNode((p2.val+flag)%10)
                flag = (p2.val+flag) >=10
                movehead.next = tmp
                movehead = movehead.next
                p2=p2.next

        if p1 != None and p2 == None:
            while p1:
                tmp = ListNode((p1.val+flag)%10)
                flag = (p1.val+flag) >=10
                movehead.next = tmp
                movehead = movehead.next
                p1=p1.next

        if flag:
            tmp = ListNode(1)
            movehead.next = tmp
        return head


if __name__ == '__main__':
    l1=ListNode(2)
    l12=ListNode(4)
    l13=ListNode(3)

    l2=ListNode(5)
    l22=ListNode(6)
    l23=ListNode(8)

    l1.next=l12
    l12.next=l13
    l2.next=l22
    l22.next=l23

    p=l1
    while p != None:
        print(p.val)
        p=p.next

    print("    ")

    p=l2
    while p != None:
        print(p.val)
        p=p.next

    print("    ")


    solu=Solution()
    l3=solu.addTwoNumbers(l1,l2)

    while l3 != None:
        print(l3.val)
        l3=l3.next


