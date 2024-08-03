import unittest
from textnode import TextNode, TEXT_TYPE_TEXT, TEXT_TYPE_IMAGE, TEXT_TYPE_BOLD, TEXT_TYPE_ITALIC, TEXT_TYPE_CODE, TEXT_TYPE_LINK
from split_images_and_links import split_nodes_link, split_nodes_images, split_nodes_bold, split_nodes_italic

def text_to_textnodes(text_input):
	nodes = [TextNode(text_input, TEXT_TYPE_TEXT)]
	nodes = split_nodes_link(nodes)
	nodes = split_nodes_images(nodes)
	nodes = split_nodes_bold(nodes)
	nodes = split_nodes_italic(nodes)

	return nodes


sample_text = "This is **bold** and this is *italic* and a [link](https://boot.dev)"
nodes = text_to_textnodes(sample_text)
for node in nodes:
	print(node.type, node.text)
