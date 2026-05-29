from textnode import *

def split_nodes_delimiter(old_nodes : list[Textnode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes=[]
    for node in old_nodes:
    
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
    
        if len(parts)%2 == 0 :
            raise ValueError("invalid Markdown: formatted section not closed")
    
        for i, part in enumerate(parts):
            if i%2==0:
                new_node = TextNode(part, TextType.TEXT)
            else:
                new_node = Textnode(part, text_type)
            new_nodes.append(new_node)

    return new_nodes