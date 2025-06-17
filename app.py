import json

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def load_posts():
    """
    loads the posts from the JSON database.
    :return: the list of posts dictionary's.
    """
    try:
        with open('storage/storage.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_posts(posts):
    """ Saves new data to the JSON database."""
    with open('storage/storage.json', 'w') as file:
        json.dump(posts, file, indent=2)



@app.route('/')
def index():
    """
    The index page.
    :return: the index page with all the blog posts.
    """
    # add code here to fetch the job posts from a file
    blog_posts = load_posts()

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    The add page, adds posts to the blog.
             GET: show the add page form.
            POST: add a new post to the blog.
    :return:
            POST: redirect to index.html
            GET: add.html form

    """
    if request.method == 'POST':
        # Get data from the form
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        # Load existing data
        blog_posts = load_posts()

        # Create new post
        new_post = {
            'id': blog_posts[-1]['id'] + 1 if blog_posts else 1,
            'author': author,
            'title': title,
            'content': content,
        }
        blog_posts.append(new_post)

        save_posts(blog_posts)

        # Redirect home after submission
        return redirect(url_for('index'))

    # GET: Show form
    return render_template('add.html')


@app.route('/delete/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    """
    The delete page, deletes a post from the blog.
    :param post_id: the id of the post do delete.
    :return: redirect to index.html
    """
    try:
        post_id = int(post_id)
    except ValueError:
        return render_template('index.html', message="Invalid post ID.")

    blog_posts = load_posts()

    # Check if the post exists
    updated_posts = [post for post in blog_posts if post['id'] != post_id]

    if len(updated_posts) == len(blog_posts):
        error_message = "Can't delete this post."
        return render_template('index.html', posts=blog_posts, message=error_message)

    # Save the updated post list
    save_posts(updated_posts)

    return redirect(url_for('index'))


@app.route('/update/<post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    """
    The update page, updates a post from the blog.
    :param post_id: the id of the post to update.
    :return:
            GET: show the update.html form.
            POST: redirect index.html
    """
    # Load all blog posts
    blog_posts = load_posts()

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
        save_posts(blog_posts)

        return redirect(url_for('index'))

    # Show the update form
    return render_template('update.html', post=post)


@app.route('/like/<post_id>', methods=['GET', 'POST'])
def like_post(post_id):
    """
    The like page, likes a post from the blog and counts the likes.
    :param post_id: the id of the post to like.
    :return: redirect ti index.html
    """
    try:
        post_id = int(post_id)
    except ValueError:
        return render_template('index.html', message="Invalid post ID.")

    # Load all blog posts
    blog_posts = load_posts()

    # Find the post by ID
    post_found = False
    for post in blog_posts:
        if post['id'] == post_id:
            # Make sure 'likes' field exists
            post['likes'] = post.get('likes', 0) + 1
            post_found = True
            break

    if not post_found:
        return "Post not found", 404

    save_posts(blog_posts)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
