class Node:
    def __init__(self, val):
        self.val  = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
            
    def push(self, newVal):
        newNode = Node(newVal) # allocates node
        newNode.next = self.head # make next of new nodes as head
        self.head = newNode # make head point to new nodes
        
    def insertAfter(self, prevNode, newVal):
        if prevNode:
            newNode = Node(newVal) # allocates node
            newNode.next = prevNode.next # set new node next to prev node next
            prevNode.next = newNode # set prev node next equal to new node
        else: # prev node does not exist
            return
    
    def append(self, newVal):
        newNode = Node(newVal) # allocates node
        if self.head:
            lastNode = self.head
            while lastNode.next: # iterate to last node o(N)
                lastNode = lastNode.next
            lastNode.next = newNode # set the new node to the next of the last node
        else:
            self.head = newNode
            
        
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6) # 6 -> none
    llist.push(7) # 7 -> 6 -> none
    llist.push(1) # 1 -> 7 -> 6 -> none
    llist.append(4) # 1 -> 7 -> 6 -> 4 -> none
    
    llist.insertAfter(llist.head.next, 8)
    
    llist.printList()
    