from textnode import *
import os
import shutil
from gencontent import *
import sys

def main():

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

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
                


main()