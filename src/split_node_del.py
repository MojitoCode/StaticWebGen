from textnode import TextNode, TEXT_TYPE_TEXT, TEXT_TYPE_CODE

def split_nodes_delimiter(node_list, delimiter, text_type):
	new_nodes = []

	for node in node_list:
		if node.text_type != TEXT_TYPE_TEXT:
			new_nodes.append(node)
		else:
			strings = node.text.split(delimiter)
			if len(strings) % 2 == 0:
				raise ValueError("Unmatched delimiter found in text: " + node.text)
			for i, string in enumerate(strings):
				if i % 2 == 0:
					new_nodes.append(TextNode(string,TEXT_TYPE_TEXT, node.url, node.href, node.src, node.alt))
				else:
					new_nodes.append(TextNode(string, text_type, node.url, node.href, node.src, node.alt))
	return new_nodes
