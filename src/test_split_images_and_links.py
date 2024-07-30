import unittest
from textnode import TextNode, TEXT_TYPE_LINK, TEXT_TYPE_TEXT, TEXT_TYPE_IMAGE
from split_images_and_links import split_nodes_link, split_nodes_images

class TestSplitNodesLink(unittest.TestCase):
	def test_split_nodes_link(self):
		original_node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
			TEXT_TYPE_TEXT,
		)

		expected_nodes = [
			TextNode("This is text with a link ", TEXT_TYPE_TEXT),
			TextNode("to boot dev", TEXT_TYPE_LINK, url="https://www.boot.dev"),
			TextNode(" and ", TEXT_TYPE_TEXT),
			TextNode("to youtube", TEXT_TYPE_LINK, url="https://www.youtube.com/@bootdotdev")
		]

		result_nodes = split_nodes_link([original_node])
		self.assertEqual(result_nodes, expected_nodes)


class TestSplitNodesImages(unittest.TestCase):
	def test_split_nodes_images(self):
		original_node = TextNode(
			"Here is an image ![boot logo](https://www.boot.dev/logo.png) and more text.",
			TEXT_TYPE_TEXT,
		)
		expected_nodes = [
			TextNode("Here is an image ", TEXT_TYPE_TEXT),
			TextNode("boot logo", TEXT_TYPE_IMAGE, url="https://www.boot.dev/logo.png"),
			TextNode(" and more text.", TEXT_TYPE_TEXT)
		]

		result_nodes = split_nodes_images([original_node])
		self.assertEqual(result_nodes, expected_nodes)

if __name__ == '__main__':
	unittest.main()
