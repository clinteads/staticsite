from block_type import markdown_to_html_node
import os

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith("# "):
            return line[2:]
    raise Exception('title not found')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path,mode='r',encoding='utf-8') as f:
        markdown_data = f.read()
    with open(template_path,mode='r',encoding='utf-8') as f:
        template = f.read()
    html_string = markdown_to_html_node(markdown_data).to_html()
    title = extract_title(markdown_data)
    html = template.replace('{{ Title }}',title).replace('{{ Content }}',html_string)
    with open(dest_path,mode='w',encoding='utf-8') as f:
        f.write(html)
    
def generate_pagees_recursive(content_dir, template_path, public_dir):
    entries = os.listdir(content_dir)
    for entry in entries:
        src = os.path.join(content_dir, entry)
        dst = os.path.join(public_dir, entry)
        if os.path.isdir(src):
            os.makedirs(dst, exist_ok=True)
            generate_pagees_recursive(src, template_path, dst)
        elif os.path.isfile(src) and src.endswith(".md"):
            if src == "index.md":
                dest_html = os.path.join(public_dir, "index.html")
            else:
                dest_html = os.path.join(public_dir, entry.replace(".md", ".html"))
            os.makedirs(public_dir, exist_ok=True)
            generate_page(src, template_path, dest_html)
