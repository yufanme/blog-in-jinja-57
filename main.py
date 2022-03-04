from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/4af156202f984d3464c3")
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/post/<post_id>')
def post(post_id):
    response = requests.get("https://api.npoint.io/4af156202f984d3464c3")
    posts = response.json()
    single_post = posts[int(post_id) - 1]
    post_body = single_post["body"]
    post_title = single_post["title"]
    return render_template("post.html", post_id=post_id, post_body=post_body, post_title=post_title)


if __name__ == "__main__":
    app.run(debug=True)
