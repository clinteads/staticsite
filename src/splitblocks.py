
def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        if len(block) == 0:
            continue
        result.append(block.strip())
    return result