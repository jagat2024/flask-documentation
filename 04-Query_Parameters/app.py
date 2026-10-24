from flask import Flask,request
app=Flask(__name__)
@app.route("/")
def home():
    return "This is the home page"
#search parameter
@app.route("/search")
def search():
    name=request.args.get("name","Guest")
    return f"hello {name}"
if __name__=="__main__":
    app.run(debug=True)
