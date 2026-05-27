import unittest

from htmlnode import *

class TextHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node=HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def text_to_html(self):
        node=HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()