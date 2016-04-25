# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import json
from sqlalchemy.orm import sessionmaker
from model import *

class SinascrapyPipeline(object):
	def __init__(self):
		engine = CreateDatabase()
		CreateTable(engine)
		self.Session = sessionmaker(bind=engine)

	@staticmethod
	def conv_timestamp(str):
		return datetime.strptime(str, '(%Y-%m-%d %H:%M:%S)')

	def process_item(self, item, spider):
		session = self.Session()

		title = item["title"][0]
		article = ''.join(item["article"])
		timestamp = SinascrapyPipeline.conv_timestamp(item["timestamp"][0])

		new_blog = Post(title=title, article=article, timestamp=timestamp)
		
		try:
			session.add(new_blog)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item













