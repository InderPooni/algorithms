from linkedlist import Node, LinkedList

class Solution:
	def __init__(self, head):
		self.head = head
	
	def find_middle_element(self):
		slow_pointer = self.head
		fast_pointer = self.head

		while fast_pointer and fast_pointer.next:
			slow_pointer = slow_pointer.next
			fast_pointer = fast_pointer.next.next
		
		return slow_pointer.data
	
	"""
		Given a singly linked list and a key, count the number of occurrences of the given key in the linked list. 
		For example, if the given linked list is 1->2->1->2->1->3->1 and the given key is 1, then the output should be 4.
	"""
	def find_occurrences(self, key):
		counter = 0
		curr = self.head

		while curr:
			if curr.data == key:
				counter += 1
			
			curr = curr.next
		
		return counter

	"""
		Given a linked list, check if the linked list has loop or not. 
			-> if null is reached return false
			-> (Approach 1): use hash table: compute the hash every time, if curr points to a node in hashtable return true
			-> (Approach 2): Floyd's Cycle-Finding Algorithm
	"""
	def find_loop(self):
		s = set()
		curr = self.head

		while curr:
			
			if curr in s:
				return True
			
			s.add(curr)
			curr = curr.next
		
		return False
	
	def floyd_cycle_finding(self):
		slow = self.head
		fast = self.head

		while slow and fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				return True
		
		return False

	def cycle_length(self):
		#find the cycle
		if self.head is None:
			return 0
		
		slow = self.head
		fast = self.head
		flag = 0

		while slow and slow.next and fast and fast.next and fast.next.next:
			if slow == fast and flag != 0:
				count = 1

				slow = slow.next

				while slow != fast:
					count += 1
					slow = slow.next
				
				return count
			
			flag = 1
			slow = slow.next
			fast = fast.next.next
		
		return 0

	
	"""
		is_palindrome(self):
		-> Approach 1: Use a stack, loop again, pop stack and compare the nodes
		-> Approach 2: Reverse Second half of the linked list , compare both halves, reverse and join second half back
	"""
	def is_palindrome(self):
		curr = self.head
		stack = []

		while curr:
			stack.append(curr.data)
			curr = curr.next
		
		x = self.head

		while x and len(stack) > 0:
			val = stack.pop()

			if x.data != val:
				return False
			
			x = x.next
		
		return True
	
	def is_palindrome_better(self):
		slow , fast , prev, temp_var = self.head , self.head , None, self.head

		while fast and fast.next:
			slow , fast = slow.next , fast.next.next

		prev, slow , prev.next = slow , slow.next, None

		while slow:
			tmp = slow.next

			slow.next, prev, slow = prev , slow , tmp
		
		fast , slow = temp_var , prev

		while slow:
			if slow.data != fast.data:
				return False
			
			fast , slow = fast.next , slow.next
		
		return True


	def remove_duplicates(self):
		curr = self.head

		if curr is None:
			return
		
		while curr.next:
			if curr.data == curr.next.data:
				curr.next = curr.next.next
			else:
				curr = curr.next
	
	"""
		Remove Duplicates Unsorted Linked List
		Approach 1: Use hash-set O(n) Time O(n) space
	"""
	def remove_duplicates_unsorted(self, head):
		if head is None or head.next is None:
			return head
	
		s = set()

		curr = head

		s.add(curr.data)

		while curr.next:
			if curr.next.data in s:
				curr.next = curr.next.next
			else:
				s.add(curr.data)
				curr = curr.next

		return head
	
	def remove_elements(self , val):
		curr = self.head

		if curr is None or curr.next is None:
			return curr
		
		while curr.next:
			if curr.val == val:
				x = curr.next
				curr = None
				curr = x
			
			elif curr.next.val == val:
				curr.next = curr.next.next
			else:
				curr = curr.next
		
		return head

	def swap_nodes_without_swapping_data(self, x , y):
		if x == y:
			return

		currX , prevX , currY , prevY = self.head , None , self.head , None

		while currX != None and currX.data != x :
			prevX = currX
			currX = currX.next
		
		while currY != None and currY.data != y:
			prevY = currY
			currY = currY.next
		
		if currY == None or currX == None:
			return
		
		# if x is head reassign head to current Y

		if prevX != None:
			prevX.next = currY
		else:
			self.head = currY
		
		if prevY != None:
			prevY.next = currX
		else:
			self.head = currX

		temp = currX.next
		currX.next = currY.next
		currY.next = temp

	#optimize above solution to run in one loop
	def swap_nodes_optimized(self,x ,y):
		# 1 2 3 4 5 6 7 
		# 1 2 4 3 5 6 7
		if x == y:
			return
		curr = self.head

		prev_x = None
		prev_y = None

		while curr.next != None:
			if curr.next.data == x:
				prev_x = curr
			elif curr.next.data == y:
				prev_y = curr
			
			curr = curr.next
		
		if prev_x != None and prev_y != None:
			temp = prev_x.next
			prev_x.next = prev_y.next
			prev_y.next = temp

			temp = prev_x.next.next
			prev_x.next.next = prev_y.next.next
			prev_y.next.next = temp
		
		return self.head


	def pairwise_swap(self):
		# 1 2 3 4 5 6 
		# 2 1 4 3 6 5a
		curr = self.head

		if curr is None:
			return

		while curr and curr.next:
			if curr.data != curr.next.data:
				curr.data , curr.next.data = curr.next.data , curr.data
		
			curr = curr.next.next

	def move_last_node_to_front(self):
		tmp = self.head
		sec_last = None # To maintain the track of
						# the second last node

		# To check whether we have not received 
		# the empty list or list with a single node
		if not tmp or not tmp.next: 
			return

		# Iterate till the end to get
		# the last and second last node 
		while tmp and tmp.next :
			sec_last = tmp
			tmp = tmp.next

		# point the next of the second
		# last node to None
		sec_last.next = None

		# Make the last node as the first Node
		tmp.next = self.head
		self.head = tmp
	
	def intersection_two_lists(self, headA , headB):
		countA = 0
		countB = 0
		currA = headA
		currB = headB

		while currA:
			countA += 1
			currA = currA.next
		while currB:
			countB += 1
			currB = currB.next
		
		diff = abs(countA - countB)
		aBigger = countA > countB

		currA = headA
		currB = headB
		for i in range(diff):
			if aBigger:
				currA = currA.next
			else:
				currB = currB.next
		

		while currA != None and currB != None:
			if currA is currB:
				return currA.data
		
		return None

	def odd_even(self):
		pass


if __name__ == "__main__":
	llist = LinkedList(6)
		
	# swap the 2 nodes
	llist.append(5)
	llist.append(4)
	llist.append(3)
	llist.append(2)
	llist.append(1)
	print ("Linked List before moving last to front ")
	llist.display()
	s = Solution(llist.head)
	s.move_last_node_to_front()
	print ("Linked List after moving last to front ")
	llist.display()
