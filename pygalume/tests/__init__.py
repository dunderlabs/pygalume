from datetime import datetime
from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.BaseModify import Base
from models import Lyrics
from controller import DataBase


class TestBaseDb(TestCase):

	def setUp(self):
		self.engine = create_engine('sqlite:///:memory:')

		Session = sessionmaker(bind=self.engine)

		Base.metadata.create_all(self.engine)

		self.session = Session()

		self.db = DataBase(self.session)

	def tearDown(self):
		Base.metadata.drop_all(self.engine)

	def _create(self, commit=True, **kwargs):
		data = {
			'artist': 'Testudo',
			'artist_url': 'http',
			'music': 'Test',
			'music_url': 'http://', 
			'text': 'Testing',
			'translate': 'Testando',
			'artist_tag': 'testudo',
			'music_tag': 'test',
			'created_date': datetime.now().date(),
		}
		data.update(kwargs)

		lyrics = Lyrics(**data)
		
		if commit:
			self.session.add(lyrics)
			self.session.commit()

		return lyrics
	