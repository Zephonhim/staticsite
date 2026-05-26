from textnode import *

def main():

    print("hello world")
    Node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(f"{Node}")

main()