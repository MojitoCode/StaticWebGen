class TextNode:
	def __init__(self, text, text_type, url=None, href=None, src=None, alt=None):
		self.text = text
		self.text_type = text_type
		self.url = url
		self.href = href
		self.src = src
		self.alt = alt

	def __eq__(self, other):
		return (
			self.text == other.text and
			self.text_type == other.text_type and
			self.url == other.url
		)

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
#define textnode types - constants
TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"
