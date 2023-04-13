from flask_login import UserMixin
from sqlalchemy import Integer, String, Boolean, Column
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from blog.models.database import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False, default="", server_default="")
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    _password = Column(String(100), nullable=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    author = relationship("Author", uselist=False, back_populates="user")

    def __init__(self, username, email, first_name=None, last_name=None, is_staff=False):
        self.username = username
        self.is_staff = is_staff
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return check_password_hash(self._password, password)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
