import json

blog_posts = [
    {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
    {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'}
]

with open('storage.json', 'w') as file:
    json.dump(blog_posts, file, indent=4)
