import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    with open('storage/storage.json', 'r') as file:
        blog_posts = json.load(file)

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get data from the form
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        # Load existing data
        with open('storage/storage.json', 'r') as file:
            blog_posts = json.load(file)

        # Create new post
        new_post = {
            'id': blog_posts[-1]['id'] + 1 if blog_posts else 1,
            'author': author,
            'title': title,
            'content': content,
        }
        blog_posts.append(new_post)

        with open('storage/storage.json', 'w') as file:
            json.dump(blog_posts, file, indent=4)

        # Redirect home after submission
        return render_template('index.html', posts=blog_posts)

    # GET: Show form
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
