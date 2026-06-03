from textnode import *
import os
import shutil

def main():

    print("hello world")
    Node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(f"{Node}")


def copy_directory(source, destination):
    
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            copy_directory(source_path, destination_path)
                
copy_directory("static", "public")

main()