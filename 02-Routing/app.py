#multiple routing example
from flask import Flask
app=Flask("__name__")
@app.route('/')
def home():
    return "welcome to the home page"
@app.route('/about')
def about():
    return "welcome to about us"
#routing dynamic 
@app.route('/users')
def users():
    return "welcome to the user page"
@app.route('/user/<name>')
def user(name):
    return f"hello {name}"
@app.route("/student/<name>/<course>")
def course(name,course):
    return f" the student {name} is learning {course}"
@app.route('/contact')
def contact():
    return "welcome to contact page"
if __name__=="__main__":
    app.run(debug=True)

#static and dynamic routing
