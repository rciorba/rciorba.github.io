import os
import os.path

from collections import defaultdict

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown2 import markdown_path


def process_folder(path, tags, template_env):
    items = [i for i in os.scandir(path)]
    names = set(i.name for i in items)
    for item in items:
        # print(">", item.path)
        if '.nogen' in names:
            return
        name = item.name
        if item.is_file():
            if name.endswith(".md") and not (name.startswith(".") or name.startswith("WIP")):
                print(item.path)
                content = process(item.path, tags, template_env)
                html_fname = item.path[:-3] + '.html'
                print(html_fname)
                with open(html_fname, 'w') as fd:
                    fd.write(content)
        elif item.is_dir():
            if not name.startswith("."):
                process_folder(item.path, tags, template_env)


def process(content, tags, template_env):
    post = markdown_path(
        content, extras=["fenced-code-blocks", "metadata", "toc"])
    post_tags = [t.strip() for t in post.metadata.get("tags", "").split(",")]
    template = template_env.get_template("post.html")
    print(post)
    return template.render(post=str(post), tags=post_tags, toc=post.toc_html)


def generate():
    tags = defaultdict(int)
    env = Environment(
        loader=FileSystemLoader('generator/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    return process_folder(".", tags=tags, template_env=env)


if __name__ == "__main__":
    import sys
    generate()
