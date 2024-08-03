from textnode import TextNode, TEXT_TYPE_TEXT, TEXT_TYPE_LINK, TEXT_TYPE_IMAGE, TEXT_TYPE_CODE, TEXT_TYPE_BOLD, TEXT_TYPE_ITALIC
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_link(old_nodes):
	newList = []
	for node in old_nodes:
		links = extract_markdown_links(node.text)


		if not links:
			newList.append(node)
		else:
			remainder_text = node.text
			for link_txt, link_url in links:
				before, link_w_brackets_and_url, remainder_text = remainder_text.partition(f"[{link_txt}]({link_url})")

				if before:
					newList.append(TextNode(before, TEXT_TYPE_TEXT))
				newList.append(TextNode(link_txt, TEXT_TYPE_LINK, url=link_url))
			if remainder_text:
				newList.append(TextNode(remainder_text, TEXT_TYPE_TEXT))
	return newList



def split_nodes_images(old_nodes):
	newList = []
	for node in old_nodes:
		images = extract_markdown_images(node.text)
		if not images:
			newList.append(node)
		else:
			remainder_text = node.text
			for image_alt, image_url in images:
				before, image_w_brackets_and_url, remainder_text = remainder_text.partition(f"![{image_alt}]({image_url})")
				if before:
					newList.append(TextNode(before, TEXT_TYPE_TEXT))
				newList.append(TextNode(image_alt, TEXT_TYPE_IMAGE, url=image_url))
			if remainder_text:
				newList.append(TextNode(remainder_text, TEXT_TYPE_TEXT))
	return newList


def split_nodes_bold(old_nodes):
	sections = []
	while '**' in old_nodes:
		before, rest = old_nodes.split('**', 1)
		bold_text, after = rest.split('**', 1)
		sections.append(('text', before))
		sections.append(('bold', bold_text))
		old_nodes = after
	if old_nodes:
		sections.append(('text', old_nodes))
	return sections


def split_nodes_italic(old_text):
	sections = []
	while '*' in old_text:
		before, rest = old_text.split('*', 1)
		italic_text, after = rest.split('*', 1)
		sections.append(('text', before))
		sections.append(('italic', italic_text))
		old_nodes = after
	if old_nodes:
		sections.append(('text', old_nodes))
	return sections


