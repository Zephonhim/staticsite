import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_difftext(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
        node2 = TextNode("This is not a text node", TextType.BOLD,"https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_difftype(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC,"https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_diffurl(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")    

if __name__ == "__main__":
    unittest.main()