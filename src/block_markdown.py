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