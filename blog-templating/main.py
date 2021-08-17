from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c37f7c7d97c9c6067326"
response = requests.get(blog_url)
response.raise_for_status()
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    post_index = blog_id - 1
    return render_template("post.html", posts=all_posts, index=post_index)


if __name__ == "__main__":
    app.run(debug=True)
