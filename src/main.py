from textnode import TextNode, TextType
import os
import shutil
from gencontent import generate_page, generate_pagees_recursive

def copy_stuff(source, destination):
    if (os.path.exists(destination)):
        shutil.rmtree(destination)
        print(f"Removing {destination}")
    os.mkdir(destination)
    paths = os.listdir(source)
    for p in paths:
        src = os.path.join(source,p)
        dst = os.path.join(destination,p)
        if os.path.isfile(src):
            print(src, "is a file with destination ", dst)
            shutil.copy(src,dst)
        else:
            print(src, "is a directory with destination ", dst)
            if not os.path.exists(dst):
                print("Creating directory ", dst)
                os.mkdir(dst)
            copy_stuff(src,dst)
    pass

def main():
    testNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(testNode)

if __name__ == "__main__":
    main()
    copy_stuff('./static','./public')
    generate_pagees_recursive('content','template.html','public')


