
from textnode import TextNode, TextType

from extractions import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        text = node.text
        matches = extract_markdown_images(text)
        current_text = text
        for match in matches:
            link_text = match[0]
            link_url = match[1]
            split_string = f"![{link_text}]({link_url})"
            parts = current_text.split(split_string,1)
            if len(parts[0]) > 0:
                result.append(TextNode(parts[0],TextType.TEXT))
            result.append(TextNode(link_text,TextType.IMAGE,link_url))
            if len(parts[1]) > 0:
                current_text = parts[1]
            else:
                current_text = ""
        if len(current_text) > 0:
            result.append(TextNode(current_text,TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        text = node.text
        matches = extract_markdown_links(text)
        current_text = text
        for match in matches:
            link_text = match[0]
            link_url = match[1]
            split_string = f"[{link_text}]({link_url})"
            parts = current_text.split(split_string,1)
            if len(parts[0]) > 0:
                result.append(TextNode(parts[0],TextType.TEXT))
            result.append(TextNode(link_text,TextType.LINK,link_url))
            current_text = parts[1]
        if len(current_text) > 0:
            result.append(TextNode(current_text,TextType.TEXT))
    return result