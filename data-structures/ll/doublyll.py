class Node:
	def __init__(self, data, prev = None, next = None):
		self.next = next
		self.prev = prev
		self.data = data


class DoublyLinkedList:
	def __init__(self):
		self.head = head

	
	def prepend(self, data):
		curr = self.head
		new_node = Node(data = data)

		if curr is None:
			self.head = new_node
			return
		
		new_node.next = curr
		new_node.prev = None
		curr.prev = new_node
	
	def append(self, data):
		curr = self.head

		new_node = Node(data = data , prev = None, next = None)

		if not curr:
			self.head = new_node
			return
		

		while curr.next:
			curr = curr.next
		
		curr.next = new_node
		new_node.prev = curr
	

	def insert_after(self , previous , data):
		pass

