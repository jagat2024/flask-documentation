from flask import Flask,request
app=Flask(__name__)
@app.route("/")
def home():
    return "This is the home page"
#search parameter
@app.route("/search")
def search():
    name=request.args.get("name","Guest")
    course=request.args.get("course","unknown")
    return f"hello {name} u are stuyding {course}"
if __name__=="__main__":
    app.run(debug=True)
