from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))
    email = db.Column(db.String(50), unique = True)
    is_active = db.Column(db.Boolean())

    def _init_(self, username, password, email, is_active):
        self.username = username
        self.password = password
        self.email = email
        self.is_active = is_active

    def __repr__(self):
        return '<User %r>' % self.username
