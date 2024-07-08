from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, None, props)  # Pass None for children, as LeafNode should not have children

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
        else:
            props = self.props_to_html()  # Convert props to HTML attributes
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
