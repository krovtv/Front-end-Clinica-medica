from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("login.html")

@app.get("/home")
def home():
    return render_template("home.html")

@app.get("/signup")
def signup():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)