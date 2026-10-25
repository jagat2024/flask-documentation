from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    name="jagat"
    course="Btech cse"
    city="kolkata"
    price=20
    courses=["python","Flask","FASTAPI","Django","Machine Learning"]
    return render_template("index.html",name=name,course=course,city=city,price = price,courses=courses)


   
if __name__=="__main__":
    app.run(debug=True)