import unittest
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_typeheading(self):
        block = "# this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_typefalseheading(self):
        block = "######## this is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_typeulist(self):
        block = "- this\n- is\n- an\n- unordered list"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
    
    def test_block_to_block_typeuquote(self):
        block = ">this\n>is\n>a\n>quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_block_to_block_typeolist(self):
        block = "1. this\n2. is\n3. an\n4. ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
    
    def test_block_to_block_typefalseolist(self):
        block = "1. this\n2. is\n4. an\n5. ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)