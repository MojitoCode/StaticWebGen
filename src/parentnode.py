from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children):
		super().__init__(tag=tag, value=None)

		if not children:
			raise ValueError("Children must have a value.")
		self.children = children

	def to_html(self):
		#check if the tag or children are empty - return an error if they are
		if not self.tag:
			raise ValueError("Value is required")
		if not self.children:
			raise ValueError("Children is required")
		
		#create opening tag
		html_string = f"<{self.tag}>"
		
		#tag content - append each child item to the html string
		for child in self.children:
			html_string += child.to_html()
		
		#create close tag
		html_string += f"</{self.tag}>"

		#return the completed html string
		return html_string
