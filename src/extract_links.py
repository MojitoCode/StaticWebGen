import re
def extract_markdown_images(text):
	reg_pattern = r"!\[(.*?)\]\((.*?)\)"
	matches = re.findall(reg_pattern, text)

	images = []

	for match in matches:
		alt_text, url = match
		images.append((alt_text, url))

	return images



def extract_markdown_links(text):
	reg_pattern = r"\[(.*?)\]\((.*?)\)"
	matches = re.findall(reg_pattern, text)

	links = []

	for match in matches:
		alt_text, url = match
		links.append((alt_text, url))

	return links


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
