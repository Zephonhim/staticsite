import os
from block_markdown import *

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise Exception("no title markdown found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content = os.listdir(dir_path_content)
    for each in content:
        each_path = os.path.join(dir_path_content, each)
        dest_each_path = os.path.join(dest_dir_path, each)
        if os.path.isfile(each_path) and each_path[-3:] == ".md":
            dest_each_html = dest_each_path.replace(".md", ".html")
            generate_page(each_path, template_path, dest_each_html, basepath)
        else :
            generate_pages_recursive(each_path, template_path, dest_each_path, basepath)