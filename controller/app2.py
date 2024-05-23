from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app2 = Flask(__name__)
# Correct the URI, ensure the username and database name is correct
app2.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Loving%4076@localhost/musicapp'
db = SQLAlchemy(app2)

# Create model
class UpdateProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Our columns
    Username = db.Column(db.String(100), nullable=False)  # string max of 100
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):  # string representation of itself
        return f"Username: {self.Username}"

# Creating APIs below, route is an endpoint to get different type of data inside a flask
@app2.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }    

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200  # return JSON data to user and status code 200 for success

@app2.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json() #user submit to us json data for creating the user name

    return jsonify(data), 201  # return back to user to show the create user was successful

@app2.route('/playlists', methods=['POST'])
def create_playlists():
    data = request.get_json() #user submit to us json data for creating the user name

    return jsonify(data), 201  # return back to user to show the create user was successful

@app2.route("/update-music-history", methods=["PUT"])
def update_music_history():
    data = request.get_json() # User submits JSON data for updating music history
    # Your code to update the music history goes here

    return jsonify(data), 200  # Return back to user to show the music history update was successful

@app2.route("/update-playlist-tracks", methods=["PUT"])
def update_playlist_tracks():
    data = request.get_json() # User submits JSON data for updating playlist tracks
    # Your code to update the playlist tracks goes here

    return jsonify(data), 200  # Return back to user to show the playlist tracks update was successful

@app2.route("/update-tracks", methods=["PUT"])
def update_tracks():
    data = request.get_json() # User submits JSON data for updating tracks
    # Your code to update the tracks goes here

    return jsonify(data), 200  # Return back to user to show the tracks update was successful


from flask import request, jsonify
#from your_module import UpdateProfile, db  # Assuming you have your model and db imported properly

@app2.route('/update_profile', methods=['POST'])
def create_username():  # Corrected function name to follow PEP 8 naming conventions
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    username = request.json.get('Username')  # Corrected variable name to follow PEP 8 naming conventions
    if not username:
        return jsonify({"error": "No username provided"}), 400

    update_profile = UpdateProfile(username=username)  # Corrected variable name to follow PEP 8 naming conventions
    db.session.add(update_profile)
    db.session.commit()
    return jsonify({"message": "Profile created", "username": username}), 201



if __name__ == '__main__':
    app2.run(debug=True)
