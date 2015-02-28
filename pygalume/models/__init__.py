from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .lyrics import Lyrics
from .BaseModify import Base

engine = create_engine('sqlite:///banco.db')

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = Session()
