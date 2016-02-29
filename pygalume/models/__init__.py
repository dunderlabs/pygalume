from .lyrics import Lyrics, db


if 'lyrics' not in db.get_tables():
    db.create_table(Lyrics)
