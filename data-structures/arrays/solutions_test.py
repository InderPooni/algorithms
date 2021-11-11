import unittest
from array_leetcode import Solution

class TestArraySolutions(unittest.TestCase):
    s = Solution()

    def test_is_panagram(self):
        sentence1 = 'thequickbrownfoxjumpsoverthelazydog'
        output1 = True

        self.assertEqual(self.s.check_if_panagram(sentence1) , True)
    
    def panagram_false(self):
        sentence = 'leetcode'
        output = False
        self.assertEqual(self.s.check_if_panagram(sentence), output)

if __name__ == '__main__':
    unittest.main()