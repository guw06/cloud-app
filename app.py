from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Cloud Technologies Laboratory 2</h1>
    <p>My first Docker application</p>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This is a Flask application running in Docker.</p>
    """

@app.route("/contact")
def contact():
    return """
    <h1>Contact</h1>
    <p>Email: student@example.com</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
