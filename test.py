from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("homepage.html")
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)