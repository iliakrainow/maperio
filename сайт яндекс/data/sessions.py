import sqlalchemy
from .db_session import SqlAlchemyBase


class Session(SqlAlchemyBase):
    __tablename__ = 'sessions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    hashed = sqlalchemy.Column(sqlalchemy.String, nullable=True)
