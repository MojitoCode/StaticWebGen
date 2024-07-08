import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
	def test_props_to_html_with_values(self):
		node = HTMLNode(tag="a", value="Click Here", props={"href": "https://www.google.com", "target": "_blank"})
		expected_output = ' href="https://www.google.com" target="_blank"'
		self.assertEqual(node.props_to_html(), expected_output)
	def test_props_to_html_empty(self):
		node = HTMLNode(tag="p", value="Hello World", props={})
		expected_output = ''
		self.assertEqual(node.props_to_html(), expected_output)
	def test_props_to_html_none(self):
		node = HTMLNode(tag="div", value="Content")
		expected_output = ''
		self.assertEqual(node.props_to_html(), expected_output)


class TestLeafNode(unittest.TestCase):
	def test_leaf_node_basic(self):
		leaf = LeafNode(tag="p", value="This is a paragraph.")
		self.assertEqual(leaf.to_html(), "<p>This is a paragraph.</p>")
	def test_leaf_node_values(self):
		leaf = LeafNode(tag="a", value="Click Me!", attrs={"href": "https://www.example.com"})
		self.assertEqual(leaf.to_html(), '<a href="https://www.example.com">Click me!</a>')
	def test_leaf_node_tagless(self):
		leaf = LeafNode(tag=None, value="Just some text.")
		self.assertEqual(leaf.to_html(), "Just some text.")
	def test_leaf_node_empty(self):
                with self.assertRaises(ValueError) as context:
			leaf = LeafNode(tag="span", value=None)
		self.assertTrue('LeafNode must have a value' in str(context.exception))


if __name__ == "__main__":
	unittest.main()
