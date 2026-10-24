
from flask import Flask
from uuid import UUID
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page Jagat"

@app.route("/contact-us")
def contact():
    return "This is our contact page brother"

@app.route("/users")
def users():
    return "Hello user"

# String URL converter
@app.route("/user/<string:name>")
def name(name):
    return f"Hello {name}"

# Integer URL converter
@app.route("/user/<int:id>")
def user(id):
    return f"User ID: {id}"

# Float URL converter
@app.route("/price/<float:price>")
def prc(price):
    return f"Price: {price}"

# Path URL converter
@app.route("/files/<path:file_path>")
def files(file_path):
    return f"File path: {file_path}"

# UUID URL converter
@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

if __name__ == "__main__":
    app.run(debug=True)
