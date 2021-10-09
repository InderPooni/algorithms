class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	
	def __init__(self, data):
		self.head = Node(data)
	
	def display(self):
		curr = self.head

		if curr is None:
			print('Print Operation invalid, Linked list is empty')
			return
		
		while curr:
			print(curr.data)
			curr = curr.next
	
	def prepend(self, data):
		n = Node(data)
		n.next = self.head
		self.head = n
	
	def append(self, data):
		n = Node(data)

		if self.head is None:
			self.head = n
			return
		
		curr = self.head

		while curr.next:
			curr = curr.next
		
		curr.next = n
	
	def push_after(self, prev_data, data):
		n = Node(data)

		curr = self.head

		if curr is None:
			print('Invalid operation, linked list is empty')
			return
		
		while curr:
			if curr.data == prev_data:
				n.next = curr.next
				curr.next = n
				return
			curr = curr.next
		

		print('Invalid operation, could not find data provided')
	
	def delete_key(self, data):
		curr = self.head

		if curr is None:
			print("Invalid operation, list is None")
			return
		
		if curr.data == data:
			self.head = curr.next
			return
		
		while curr.next:
			if curr.next.data == data:
				curr.next = curr.next.next
				return
			
			curr = curr.next
		
		print("Invalid Operation: Key not found")

	def length(self):
		curr = self.head

		if curr is None:
			return 0

		counter = 0

		while curr:
			counter += 1
			curr = curr.next

		
		return counter

	def rec_len(self, head):
		if head is None:
			return 0
		else:
			return 1 + self.rec_len(head.next)
	
	def recursive_length(self):
		return self.rec_len(self.head)

	
	def iterative_search(self, target):
		curr = self.head

		if curr is None:
			print("Linked List is None")
			return
		
		position = 1
		while curr:
			if curr.data == target:
				return position
			
			position += 1

			curr = curr.next
		
		return -1
	
	def rec_search(self, head, target, pos):
		if head is None:
			return -1
		elif head.data == target:
			return pos
		else:
			return self.rec_search(head.next, target,pos + 1)

	def recursive_search(self, target):
		return self.rec_search(self.head, target,1)

	
	def get_nth_element(self,n):
		if n == 0:
			return self.head.data
		
		curr = self.head
		c = 0

		while curr:
			if c == n:
				return curr.data
			
			c += 1
			curr = curr.next
		
		print("{} is out of the bounds of the LinkedList".format(n))
		return

	def get_nth_element_from_end(self, n):
		length = self.length()

		curr = self.head

		if curr is None:
			print("Linked List is None")
			return

		if n > length:
			print("{} is greater than the length of the list".format(n))
			return
		
		for i in range(length - n):
			curr = curr.next
			
		return curr.data


	def delete_at_position(self, idx):
		curr = self.head

		if curr is None:
			print("Invalid Operation, List is None")
			return
		
		if idx == 0:
			self.head = self.head.next
			return
		
		if idx > self.length():
			print("Position is outside of the length of ll")
			return
		
		for i in range(1, idx):
			if i + 1 == idx:
				curr.next = curr.next.next
				return
			
			curr = curr.next
	
	def delete_list(self):
		self.head = None




if __name__ == "__main__":

	llist = LinkedList(20)
	llist.prepend(4)
	llist.prepend(15)
	llist.prepend(35)
	print(llist.get_nth_element_from_end(4))
	
	# 35 15 4 20