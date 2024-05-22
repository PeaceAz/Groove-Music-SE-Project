from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:Ogechukwu@76@localhost/musicapp'
db = SQLAlchemy(app2)


# Create model
class Update_profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)  #OUr columns
    Username = db.Column(db.String(100), nullable=False) #string max of 100
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

   def_repr__(self):   # string representation of itself
       return f"Username: {self.Username}" 

    def__init__(self, Username):
       self.Username = Username

@app.route('/')
def hello():
    return 'hey!'

if __name__ == '__main__':
    app.run()

