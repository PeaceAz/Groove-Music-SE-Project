from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app2 = Flask(__name__)
# Correct the URI
app2.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Loving%4076@localhost/musicapp'
db = SQLAlchemy(app2)

# Create model
class Update_profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Our columns
    Username = db.Column(db.String(100), nullable=False)  # string max of 100
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):  # string representation of itself
        return f"Username: {self.Username}"

    def __init__(self, Username):
        self.Username = Username

@app2.route('/')
def hello():
    return 'hey!'

if __name__ == '__main__':
    app2.run()

