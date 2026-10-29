class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None


class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.head = Node(-1,-1)
    self.tail = Node(-1,-1)
    self.head.next = self.tail
    self.tail.prev = self.head
  
  
  def _add(self, node : Node):
    # Add a node after the head
    # (most recently used position).
    next_node = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = next_node
    next_node.prev = node
  
  def _remove(self, node : Node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
  
  
  def get(self, key : int) -> int:
    # Get the value for a given key
    if key not in self.cache:
      return -1
    
    node = self.cache[key]
    self._remove(node)
      
  
  
  def put(self, key : int, value: int):


if __name__ == "__main__":
  
    
    