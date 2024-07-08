class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("Error: Sub-classes should implement this!")

	def props_to_html(self):
		if not self.props:
			return ""
		
		props_str = ""
		for key, value in self.props.items():
			props_str += f' {key}="{value}"'
		return props_str

	def __repr__(self):
		return f"HTMLNode - Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"


class LeafNode(HTMLNode):
	def __init__(self, tag, value, attrs=None):
		super().__init__(tag, attrs)
		if attrs is None:
			attrs = {}
		self.value = value

		if self.value is None:
			raise ValueError("LeafNode must have a value")

	def to_html(self):
		if self.value is None:
			raise ValueError("LeafNode must have a value")
		
		if self.tag is None:
			return self.value
		
		html = f"<{self.tag}"
		if self.attrs:
			for attr, val in self.attrs.items():
				html += f' {attr}="{val}"'
		html += f">{self.value}</{self.tag}>"
		
		return html
