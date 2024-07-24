import unittest
from textnode import TextNode, TEXT_TYPE_TEXT, TEXT_TYPE_CODE
from split_node_del import split_nodes_delimiter

def test_split_nodes_delimiter():
	node = TextNode("This is a text `code block` in a sentence", TEXT_TYPE_TEXT)
	delimiter = "`"
	text_type = TEXT_TYPE_CODE
	result = split_nodes_delimiter([node], delimiter, text_type)

	expected = [
		TextNode("This is a text ", TEXT_TYPE_TEXT),
		TextNode("code block", TEXT_TYPE_CODE),
		TextNode(" in a sentence", TEXT_TYPE_TEXT)
	]

	assert result == expected, f"Expected {expected}, but got {result}"

test_split_nodes_delimiter()
print("All tests passed!")
