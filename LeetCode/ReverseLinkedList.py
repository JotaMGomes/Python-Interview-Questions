# https://leetcode.com/problems/reverse-linked-list/
# Jose Luiz Mattos Gomes

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    # define return variable
    vReturn = None
    
    def reverseList(self, head: ListNode) -> ListNode:
      # test if head is None
      if head == None:
        # return list
        return self.vReturn
      
      # create new node and point it to actual returning head
      vAux = self.vReturn
      
      # create new head for returning list and point it to aux node
      self.vReturn = ListNode(head.val)
      self.vReturn.next = vAux
      
      # call function recursively with next node
      return self.reverseList(head.next)


    def printList(self, head: ListNode):
      vAux = head
      while vAux != None:
        print(str(vAux.val), end='-> ')
        vAux = vAux.next
      print('None')
	


s = Solution()

vHead = ListNode(1)

vPointer = ListNode(2)
vHead.next = vPointer
vPointer = vHead.next

vNewNode = ListNode(3)
vPointer.next = vNewNode
vPointer = vNewNode

vNewNode = ListNode(4)
vPointer.next = vNewNode
vPointer = vNewNode

vNewNode = ListNode(5)
vPointer.next = vNewNode
vPointer = vNewNode

s.printList(vHead)
s.printList(s.reverseList(vHead))