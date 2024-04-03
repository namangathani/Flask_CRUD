from flask import Flask
from flask import render_template
from flask import request
import os
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Food(db.Model):
    item = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    def __repr__(self):
        return "<item: {}>".format(self.item)
    
@app.route("/", methods=["GET", "POST"])
def home():
    # names=None
    if request.form:
        name = Food(item=request.form.get("item"))
        db.session.add(name)
        db.session.commit()
    items = Food.query.all()    
    return render_template("homepage.html",items=items)

@app.route("/update", methods=["POST"])
def update():
    new = request.form.get("new")
    old = request.form.get("old")
    item = Food.query.filter_by(item=old).first()
    # item.name = new
    if item:
        item.item=new
        db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    item = request.form.get("item")
    item = Food.query.filter_by(item=item).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)