from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "myqsl://myuser:myuser@db/main"


db = SQLAlchemy(app)

class product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.string(200))
    image = db.Column(db.string(200))
    
class productUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')
    

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')