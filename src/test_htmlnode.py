import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node=HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def text_to_html(self):
        node=HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")