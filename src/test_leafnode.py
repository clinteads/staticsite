import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_props_to_html_a(self):
        test_props = {
            "href": "https://www.google.com",
        }
        node = LeafNode("a", "Click me!", props=test_props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    