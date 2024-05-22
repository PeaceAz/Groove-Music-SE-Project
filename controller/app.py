from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
 
# Create model
class Update_profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)  #Our columns
    Username = db.Column(db.String(100), nullable=False) #string max of 100
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):   # string representation of itself
       return f"Username: {self.Username}" 

    def __init__(self, Username):
       self.Username = Username

@app.route('/')
def hello():
    return 'hey!'

if __name__ == '__main__':
    app.run()

