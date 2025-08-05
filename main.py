from flask import Flask,render_template,request, flash

app=Flask(__name__)
app.secret_key='10011'

@app.route("/")
def main():
    flash("Thanking You !!!","success")
    return render_template("index.html")

@app.route("/sec",methods=["GET","POST"])
def second():
    flash("OK byee...")
    return render_template("index2.html")


app.run(debug=True)