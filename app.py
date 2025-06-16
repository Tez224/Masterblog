import json

from flask import Flask, render_template, request, redirect, url_for

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


@app.route('/delete/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    try:
        post_id = int(post_id)
    except ValueError:
        return render_template('index.html', message="Invalid post ID.")

    with open('storage/storage.json', 'r') as file:
        blog_posts = json.load(file)

    # Check if the post exists
    updated_posts = [post for post in blog_posts if post['id'] != post_id]

    if len(updated_posts) == len(blog_posts):
        error_message = "Can't delete this post."
        return render_template('index.html', posts=blog_posts, message=error_message)

    # Save the updated post list
    with open('storage/storage.json', 'w') as file:
        json.dump(updated_posts, file, indent=2)

    return redirect(url_for('index'))


@app.route('/update/<post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    # Load all blog posts
    with open('storage/storage.json', 'r') as file:
        blog_posts = json.load(file)

    # Find the post by ID
    post = None
    for p in blog_posts:
        if str(p['id']) == str(post_id):
            post = p
            break

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        # Update post with form data
        post['author'] = request.form['author']
        post['title'] = request.form['title']
        post['content'] = request.form['content']

        # Save the updated list of posts
        with open('storage/storage.json', 'w') as file:
            json.dump(blog_posts, file, indent=2)

        return redirect(url_for('index'))

    # Show the update form
    return render_template('update.html', post=post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
