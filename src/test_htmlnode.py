import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
	unittest.main()
