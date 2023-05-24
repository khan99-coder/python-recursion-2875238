"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def traverse(head):
    # Base case
    if head is None:
        return
    # Recursive case
    print(head.data)
    traverse(head.next)
    return        
        
        
item1 = Node("Dog")
item2 = Node("Cat")
item3 = Node("Fish")
item1.next = item2
item2.next = item3


# traverse(item1)

head = Node("Dog", Node("Cat", Node("Fish", None)))
traverse(head)