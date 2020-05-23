from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "11df6318f394029e2669979c288eadb9"
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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("Register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful, please check username and password.", "danger")
    return render_template("Login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
