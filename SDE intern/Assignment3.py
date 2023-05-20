class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMiddle(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.data

# Example usage:
# Create a sample linked list: 0 -> 2 -> 9 -> 5 -> 3
head = Node(0)
head.next = Node(2)
head.next.next = Node(9)
head.next.next.next = Node(5)
head.next.next.next.next = Node(3)

# Call the getMiddle() function
middle_element = getMiddle(head)
print("Middle element:", middle_element)
