Flask Blog Project

Overview

This is a simple Flask-based blog application that allows users to create, update, delete, and like blog posts. Posts are stored persistently in a JSON file (storage/storage.json), enabling basic content management without a database.

Features:

- View all posts on the homepage

- Add new posts with author, title, and content

- Update existing posts

- Delete posts

- Like posts and keep count of likes per post

- Data persistence using JSON file storage

Technologies Used
- Python 3

- Flask web framework

- JSON for data storage

- HTML/CSS for templates and styling

Installation & Setup
Clone the repository:

```
git clone <repository_url>
cd <repository_folder>
```
(Optional) Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
Install dependencies:

```
pip install Flask
```
Run the Flask app:
```
python app.py
```
Open your browser and navigate to:

http://127.0.0.1:5001/
Project Structure
<pre> ```
.
├── app.py                 # Main Flask application
├── storage/
│   └── storage.json       # JSON file storing blog posts
├── templates/             # HTML templates for rendering pages
│   ├── index.html
│   ├── add.html
│   ├── update.html
│   └── ...
└── static/   
# (Optional) Static files like CSS ``` </pre>

Usage

- Visit the homepage to see all blog posts.

- Use the Add Post page to submit new blog entries.

- Use the Update and Delete buttons next to each post to modify or remove it.

- Use the Like button to increment the like count of any post.

Notes

- Data is saved in a JSON file, so concurrency issues may occur if multiple users try to modify posts simultaneously.

- This project is intended as a learning example for Flask and basic CRUD operations.

License
- MIT License (or specify your license)

