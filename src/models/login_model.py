from src.models import Base, session
from sqlalchemy import Column, ForeignKey, Integer

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'<Login {self.user_id}>'
    