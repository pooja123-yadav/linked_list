class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList(Node):
    def __init__(self):
        self.head = None
        
    def InsertAtBegining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
            
    def InsertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def InsertAtGivenIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        
        if position == index:
            self.InsertAtBegining(data)
        else:
            while(current_node.next != None and position+1 != index):
                current_node = current_node.next
                
            if current_node.next != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not found")
    
    # Update node of a linked list
		# at given position
    def updateNode(self, val, index):
        if self.head is None:
            return
        else:
            current_node = self.head
            position = 0
        
            if position == index:
                self.head.data = val
        
            while (current_node.next != None and position != index):
                position += 1
                current_node = current_node.next
        
            if current_node != None:
                current_node.data = val
            else:
                print("Index is not found")
	    
	            
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def remove_last_node(self):
        if self.head is None:
            return
        current = self.head
        while current.next.next:
            current = current.next
            
        current.next = None
        
    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head is None:
            return
        else:
            current_node = self.head
            position = 0
            if position == index:
                self.remove_first_node()
            else:
                while current_node is not None and position + 1 != index:
                    position += 1
                    current_node = current_node.next
        
                if current_node.next is not None:
                    current_node.next = current_node.next.next
                else:
                    print("Index is not found")
        
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        
        
l = LinkedList() 
l.InsertAtBegining(10)
l.InsertAtEnd(20)
l.InsertAtEnd(30)
l.InsertAtEnd(40)
l.remove_last_node()
l.remove_first_node()
l.InsertAtGivenIndex(50, 0)
l.updateNode(90,1)
l.remove_at_index(1)
print(l.printLL())

# ======================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0 
        current = head

        while current:
            count += 1
            current = current.next

        position = count - n

        if position == 0:
            return head.next

        current = head
        for _ in range(position-1):
            current = current.next

        current.next = current.next.next

        return head    
# ============================================================ optimized solution with slo and fast pointer

# Create two pointers, fastp and slowp
        fastp = head
        slowp = head

        # Move the fastp pointer N nodes ahead
        for i in range(n):
            fastp = fastp.next

        # If fastp becomes None, the Nth node from the end is the head
        if fastp is None:
            return head.next

        # Move both pointers until fastp reaches the end
        while fastp.next is not None:
            slowp = slowp.next
            fastp = fastp.next

        # Delete the Nth node from the end
        delNode = slowp.next
        slowp.next = slowp.next.next
        delNode = None

        return head


        
