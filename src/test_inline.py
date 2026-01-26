import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, text_to_textnodes

from textnode import TextNode as TN_from_textnode

# print("DEBUG class from textnode:", TN_from_textnode)
# print("DEBUG class use in inline_markedown:", type(text_to_textnodes("x")[0]))


def assert_nodes(nodes, texts, types):
    assert len(nodes) == len(texts) == len(types)
    for i, node in enumerate(nodes):
        assert node.text == texts[i]
        assert node.text_type == types[i]



class TestInline(unittest.TestCase):
    def test_inline(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        # print(result)
        expected_results = [
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
        ]
        self.assertListEqual(expected_results,result)   
