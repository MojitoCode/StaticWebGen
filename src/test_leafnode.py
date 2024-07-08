import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_basic(self):
        leaf = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph.</p>")

    def test_leaf_node_values(self):
        leaf = LeafNode(tag="a", value="Click Me!", props={"href": "https://www.example.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.example.com">Click Me!</a>')

if __name__ == '__main__':
    unittest.main()
