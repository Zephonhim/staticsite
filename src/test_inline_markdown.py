import unittest
from inline_markdown import *
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        old_nodes = [TextNode("this is **bold** text", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(old_nodes, "**", TextType.BOLD),[TextNode("this is ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT),])

    def test_italic(self):
        old_nodes = [TextNode("is this _italic_ text?",TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(old_nodes, "_", TextType.ITALIC),[TextNode("is this ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" text?", TextType.TEXT),])
    
    def test_text(self):
        old_nodes = [TextNode("this is not bold text", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter(old_nodes, "**", TextType.BOLD),[TextNode("this is not bold text", TextType.TEXT),])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnode(self):

        self.assertEqual(text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"), [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])