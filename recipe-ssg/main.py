import os
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

#with open('content/kjotbaka.md', 'r') as file:  
#    parsed_md = markdown(file.read(), extras=['metadata'])

POSTS = {}
for markdown_post in os.listdir('content'):
    file_path = os.path.join('content', markdown_post)
    with open(file_path, 'r') as file:
        POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])

env = Environment( loader = PackageLoader('main', 'templates'))
test_template = env.get_template('test.html')

for value in POSTS.values():
    data = {
        'content': value,
        'title': value.metadata['title'],
        'date': value.metadata['date']
        }
    print( test_template.render( post=data))

#print('Metadata: ', parsed_md.metadata)
#print('Content: ', parsed_md) 