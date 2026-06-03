from inline_markdown import *
from textnode import *
from enum import Enum

def markdown_to_blocks(markdown):
    splits=markdown.split("\n\n")
    stripped =[]
    for split in splits:
        strip=split.strip()
        if strip == "":
            continue
        stripped.append(strip)
    return stripped

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(text):
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if text.startswith("```\n") and text.endswith("\n```"):
        return BlockType.CODE
    lines = text.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.ULIST
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, 1)):
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    htmlnodes = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        html = text_node_to_html_node(node)
        htmlnodes.append(html)
    return htmlnodes

def paragraph_to_html_node(block):
    split = block.split("\n")
    joined = " ".join(split)
    children = text_to_children(joined)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    strip = block[level + 1:]
    children = text_to_children(strip)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    text = block[4:-3]
    node = TextNode(text, TextType.TEXT)
    children = text_node_to_html_node(node)
    code = ParentNode("code",[children])
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    lines = block.split("\n")
    linodes=[]
    for line in lines:
        children = text_to_children(line[2:])
        parent = ParentNode("li", children)
        linodes.append(parent)
    return ParentNode("ul", linodes)

def olist_to_html_node(block):
    lines = block.split("\n")
    linodes=[]
    for line in lines:
        children = text_to_children(line.split(". ",1)[1])
        parent = ParentNode("li", children)
        linodes.append(parent)
    return ParentNode("ol", linodes)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    childs = []
    for block in blocks:
        btype = block_to_block_type(block)
        if btype == BlockType.PARAGRAPH:
            node=paragraph_to_html_node(block)
            childs.append(node)
        if btype == BlockType.HEADING:
            node=heading_to_html_node(block)
            childs.append(node)
        if btype == BlockType.QUOTE:
            node=quote_to_html_node(block)
            childs.append(node)
        if btype == BlockType.CODE:
            node = code_to_html_node(block)
            childs.append(node)
        if btype == BlockType.ULIST:
            node=ulist_to_html_node(block)
            childs.append(node)
        if btype == BlockType.OLIST:
            node=olist_to_html_node(block)
            childs.append(node)
    return ParentNode("div", childs)
