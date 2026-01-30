from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def ordered_list_helper(markdown):
    count = 1
    for line in markdown.split('\n'):
        dot_index = line.find('.')
        if dot_index == -1:
            return False
        number_part = line[:dot_index]
        after_dot = line[dot_index+1:]
        if number_part.isdigit() and after_dot.startswith(" "):
            if count != int(number_part):
                return False
        count += 1
    return True
            

def block_to_block_type(markdown):
    if markdown.startswith('#'):
        for i in range(6):
            if markdown[i] == '#' and markdown[i+1] == ' ':
                return BlockType.HEADING
    if markdown.startswith('```\n'):
        return BlockType.CODE
    if markdown.startswith('>'):
        for line in markdown.split('\n'):
            if line.startswith('>'):
                continue
            else:
                return BlockType.PARAGRAPH   
        return BlockType.QUOTE
    if markdown.startswith('- '):
        for line in markdown.split('\n'):
            if line.startswith('- '):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if ordered_list_helper(markdown):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH