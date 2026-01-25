import unittest

from textnode import TextNode, TextType
from nodesplitter import split_nodes_delimiter

def assert_nodes(nodes, texts, types):
    assert len(nodes) == len(texts) == len(types)
    for i, node in enumerate(nodes):
        assert node.text == texts[i]
        assert node.text_type == types[i]



class TestNodeSplitter(unittest.TestCase):
    def test_delimiter_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert_nodes(
            new_nodes,
            ['This is text with a ','code block',' word'],
            [TextType.TEXT, TextType.CODE, TextType.TEXT]
        )