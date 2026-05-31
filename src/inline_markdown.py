from textnode import *
import re

def split_nodes_delimiter(old_nodes : list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes=[]
    for node in old_nodes:
    
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
    
        if len(parts)%2 == 0 :
            raise ValueError("invalid Markdown: formatted section not closed")
    
        for i, part in enumerate(parts):
            if i%2==0:
                new_node = TextNode(part, TextType.TEXT)
            else:
                new_node = TextNode(part, text_type)
            new_nodes.append(new_node)

    return new_nodes

def extract_markdown_images(text: str) -> list[tuple]:
    
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return images

def extract_markdown_links(text: str) -> list[tuple]:

    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for each in old_nodes:
        
        new_nodes=extract_markdown_images(each.text)
        if len(new_nodes) == 0:
                result.append(each)
                continue
        remaining_text = each.text

        for image in new_nodes:
            sections = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(image[0], TextType.IMAGE, image[1]))
            remaining_text = sections[1]
        if remaining_text != "":
            result.append(TextNode(remaining_text, TextType.TEXT))
    return result


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for each in old_nodes:
        
        new_nodes=extract_markdown_links(each.text)
        if len(new_nodes) == 0:
                result.append(each)
                continue
        remaining_text = each.text

        for link in new_nodes:
            sections = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(link[0], TextType.LINK, link[1]))
            remaining_text = sections[1]
        if remaining_text != "":
            result.append(TextNode(remaining_text, TextType.TEXT))
    return result