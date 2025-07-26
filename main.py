from flask import Flask
app=Flask(__name__)
@app.route("/")
def Hello_World():
    return "<pre>Hii I am Ronit Kumar Singh</pre>"

@app.route("/route")
def route():
    return "<p>Hii I am Ronit "

app.run(debug=True)