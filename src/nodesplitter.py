from textnode import TextType, TextNode

def is_even(num):
    return num % 2 == 0

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        node_split = node.text.split(delimiter)
        node_split_len = len(node_split)
        if is_even(node_split_len):
            raise Exception("Missing closing delimiter")
        for i in range(node_split_len):
            if is_even(i) and len(node_split[i]) > 0:
                result.append(TextNode(node_split[i], TextType.TEXT))
            elif not is_even(i) and len(node_split[i]) > 0:
                result.append(TextNode(node_split[i], text_type))
    return result

        