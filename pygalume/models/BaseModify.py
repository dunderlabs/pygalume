from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base,declared_attr


class BaseModify(object):
    """
    All the classes that inherit of Base, are created by default with an ID, and
    doesn't need set up __tablename__ attribute.
    """
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=BaseModify)
