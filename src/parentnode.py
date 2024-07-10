from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children):
		super.__init__(tag=tag, value=None)

		if not children:
			raise valueError("Children must have a value.")
		self.children = children

	def to_html():
		if not tag:
			raise valueError("Value is required")
