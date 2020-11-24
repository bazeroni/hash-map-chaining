from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]
  
  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hashed = self.hash(key)
    array_index = self.compress(hashed)
    list_at_array = self.array[array_index]
    payload = Node([key, value])
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
    list_at_array.insert(payload)

  def retrieve(self, key):
    hashed = self.hash(key)
    array_index = self.compress(hashed)
    list_at_index = self.array[array_index]
    for i in list_at_index:
      if i[0] == key:
        return i[1]
    else:
      return None
    
    if not payload is None:
      if payload[0] == key:
        return payload[1]
    else:
      return None

blossom = HashMap(len(flower_definitions))

for i in flower_definitions:
  blossom.assign(i[0], i[1])

print(blossom.retrieve('daisy'))
