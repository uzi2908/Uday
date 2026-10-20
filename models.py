from extensions import db


class Users(db.Model):
    __tablename__ = "USERS"
    id = db.Column(db.Integ)