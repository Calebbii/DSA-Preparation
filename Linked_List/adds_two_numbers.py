class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  # Dummy node to handle the result linked list
    current = dummy
    carry = 0
    
    while l1 or l2:
        # Get the values of current nodes (or 0 if the node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate the sum of current digits along with the carry
        total = val1 + val2 + carry
        
        # Update the carry for the next iteration
        carry = total // 10
        
        # Create a new node with the value equal to the remainder of total divided by 10
        current.next = ListNode(total % 10)
        
        # Move to the next nodes in both input lists if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        
        # Move to the next node in the result list
        current = current.next
    
    # Check if there's any remaining carry
    if carry:
        current.next = ListNode(carry)
    
    # Return the next node of the dummy node (head of the resulting linked list)
    return dummy.next