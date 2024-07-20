# test_text_node_to_html_node.py

import unittest
from textnode import TextNode, TEXT_TYPE_TEXT, TEXT_TYPE_BOLD, TEXT_TYPE_ITALIC, TEXT_TYPE_CODE, TEXT_TYPE_LINK, TEXT_TYPE_IMAGE
from leafnode import LeafNode
from text_node_to_html import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        text_node = TextNode(text="Sample text", text_type=TEXT_TYPE_TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, '')
        self.assertEqual(html_node.value, "Sample text")
    
    def test_text_type_bold(self):
        text_node = TextNode(text="Bold text", text_type=TEXT_TYPE_BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "Bold text")
        
    def test_text_type_italic(self):
        text_node = TextNode(text="Italic text", text_type=TEXT_TYPE_ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "Italic text")
    
    def test_text_type_code(self):
        text_node = TextNode(text="Code text", text_type=TEXT_TYPE_CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "Code text")
        
    def test_text_type_link(self):
        text_node = TextNode(text="Link text", text_type=TEXT_TYPE_LINK, href="https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props.get("href"), "https://example.com")
        
    def test_text_type_image(self):
        text_node = TextNode(text="", text_type=TEXT_TYPE_IMAGE, src="https://example.com", alt="some test text")
