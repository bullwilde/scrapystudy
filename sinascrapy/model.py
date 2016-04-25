from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, UnicodeText, Text, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

def CreateDatabase():
	return create_engine('sqlite:///sinablog2.sqlite')

# echo output to console
# db.echo = True

Base = declarative_base()


class Post(Base):
	__tablename__ = 'posts'

	id = Column(Integer, primary_key=True)
	title = Column(UnicodeText)
	article = Column(UnicodeText)
	timestamp = Column(DateTime)


	def __repr__(self):
		return u"%s" % self.title

def CreateTable(engine):
	Base.metadata.create_all(engine)

