import unittest

from block_type import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_headings(self):
        header = "# One"
        self.assertEqual(block_to_block_type(header), BlockType.HEADING)
        header = "## Two"
        self.assertEqual(block_to_block_type(header), BlockType.HEADING)
        header = "### Three"
        self.assertEqual(block_to_block_type(header), BlockType.HEADING)
        header = "#### Four"
        self.assertEqual(block_to_block_type(header), BlockType.HEADING)
        header = "##### Five"
        self.assertEqual(block_to_block_type(header), BlockType.HEADING)
        header = "###### Six"
        self.assertEqual(block_to_block_type(header), BlockType.HEADING)
        header = "####### Seven"
        self.assertEqual(block_to_block_type(header), BlockType.PARAGRAPH)
    
    def test_code_blocks(self):
        codeblock = "```\nstuff\ntwo\n```"
        self.assertEqual(block_to_block_type(codeblock),BlockType.CODE)
    
    def test_quote_block(self):
        quoteblock = ">lineone\n>linetwo>\n>linethree"
        self.assertEqual(block_to_block_type(quoteblock), BlockType.QUOTE)

    def test_unordered_block(self):
        unorderedblock = "- one\n- two\n- three"
        self.assertEqual(block_to_block_type(unorderedblock),BlockType.UNORDERED_LIST)

    def test_ordered_block(self):
        orderedblock = "1. one\n2. two\n3. three"
        self.assertEqual(block_to_block_type(orderedblock),BlockType.ORDERED_LIST)  

