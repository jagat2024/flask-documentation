#multiple routing example
from flask import Flask
app=Flask("__name__")
@app.route('/')
def home():
    return "welcome to the home page"
@app.route('/about')
def about():
    return "welcome to about us"
@app.route('/contact')
def contact():
    return "welcome to contact page"
if __name__=="__main__":
    app.run(debug=True)

