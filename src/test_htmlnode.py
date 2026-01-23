import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
    
    def test_props_None(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(),"")
    
    def test_props_empty_string(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(),"")

    def test_props_2(self):
        test_props = {
            "target": "_blank",
            "href": "https://www.google.com",
        }
        node = HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(),' target="_blank" href="https://www.google.com"')
    
    def test_repr(self):
        test_props = {
            "target": "_blank",
            "href": "https://www.google.com",
        }
        answer = "HTMLNODE(tag='h1', value='Header 1', children=[HTMLNODE(tag='None', value='None', children=None, props=None)], props={'target': '_blank', 'href': 'https://www.google.com'})"
        childnode = HTMLNode()
        children = []
        children.append(childnode)
        node = HTMLNode(tag="h1",value="Header 1",children=children,props=test_props)
        self.assertEqual(repr(node),answer)