class Solution:
	def upsideDownBinaryTree(self, root):
		if not root:
			return None
		new_root = None
		self.upside_down(root)
