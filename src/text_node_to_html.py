from textnode import TextNode, TEXT_TYPE_TEXT, TEXT_TYPE_BOLD, TEXT_TYPE_ITALIC, TEXT_TYPE_CODE, TEXT_TYPE_LINK, TEXT_TYPE_IMAGE
from leafnode import LeafNode
from htmlnode import HTMLNode

def text_node_to_html_node(text_node):
	if not isinstance(text_node, TextNode):
		raise ValueError("Input value must be a TextNode")
	
	if text_node.text_type == TEXT_TYPE_TEXT:
		return LeafNode(tag='', text=text_node.text)
	elif text_node.text_type == TEXT_TYPE_BOLD:
                return LeafNode(tag='b', text=text_node.text)
	elif text_node.text_type == TEXT_TYPE_ITALIC:
                return LeafNode(tag='i', text=text_node.text)
	elif text_node.text_type == TEXT_TYPE_CODE:
                return LeafNode(tag='code', text=text_node.text)
	elif text_node.text_type == TEXT_TYPE_LINK:
                return LeafNode(tag='a', text=text_node.text, href=text_node.href)
	elif text_node.text_type == TEXT_TYPE_IMAGE:
                return LeafNode(tag='img', text='', src=text_node.src, alt=text_node.alt)
	else:
		raise ValueError(f"Unsupported TextNode type: {text_node.text_type}")
