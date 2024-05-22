import os

class config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:Loving@76@localhost/musicapp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False