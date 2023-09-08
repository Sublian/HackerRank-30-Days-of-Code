 #Complete this method
def insert(self,head,data):   
  new_node = Node(data)
  #check head value
  if not head :
      #only works for the first value
      head = new_node
  else:
      #get the last position for adding a new value in the stack
      current = head
      while current.next:
          current = current.next
      current.next = new_node    
  return head
