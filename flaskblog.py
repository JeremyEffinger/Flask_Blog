from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Jeremy Effinger",
        "title": "First Post",
        "content": "First Post Content",
        "date_posted": "May 22, 2020",
    },
    {
        "author": "Jamie Effinger",
        "title": "Second Post",
        "content": "Second Post Content",
        "date_posted": "May 23, 2020",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
