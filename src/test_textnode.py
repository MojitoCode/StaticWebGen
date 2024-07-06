import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
	def test_eq(self):
        	node = TextNode("This is a text node", "bold")
        	node2 = TextNode("This is a text node", "bold")
        	self.assertEqual(node, node2)

	def test_url_empty(self):
		node = TextNode("This is a text node", "bold")
		self.assertIsNone(node.url)

	def test_url_with_value(self):
        	node = TextNode("This is a text node", "bold", "http://example.com")
        	self.assertEqual(node.url, "http://example.com")
    
	def test_nq(self):
        	node1 = TextNode("This is a text node", "bold", "http://example1.com")
        	node2 = TextNode("This is a text node", "bold", "http://example2.com")
        	self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
