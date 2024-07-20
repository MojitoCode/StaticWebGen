# text_node_to_html.py

from textnode import TextNode, TEXT_TYPE_TEXT, TEXT_TYPE_BOLD, TEXT_TYPE_ITALIC, TEXT_TYPE_CODE, TEXT_TYPE_LINK, TEXT_TYPE_IMAGE
from leafnode import LeafNode
from htmlnode import HTMLNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Input value must be a TextNode")

    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(tag='', value=text_node.text)
    elif text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode(tag='b', value=text_node.text)
    elif text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    elif text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode(tag='code', value=text_node.text)
    elif text_node.text_type == TEXT_TYPE_LINK:
        props = {"href": text_node.href} if text_node.href else {}
        return LeafNode(tag='a', value=text_node.text, props=props)
    elif text_node.text_type == TEXT_TYPE_IMAGE:
        props = {"src": text_node.src, "alt": text_node.alt} if text_node.src and text_node.alt else {}
        return LeafNode(tag='img', value='', props=props)
    else:
        raise ValueError(f"Unsupported TextNode type: {text_node.text_type}")
