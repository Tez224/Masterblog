import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    with open('storage/storage.json', 'r') as file:
        blog_posts = json.load(file)

    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
