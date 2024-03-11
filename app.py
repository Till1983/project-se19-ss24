from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

articles = {
    1: { 'title': 'The First Post', 'content': 'This is the first post.' },
    2: { 'title': 'The Second Post', 'content': 'This is the second post.' },
    3: { 'title': 'The Third Post', 'content': 'This is the third post.' }
}

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/posts')
def posts():
    return render_template("posts.html")

@app.route('/posts/<int:post_id>')
def post(post_id):
    post = articles.get(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)