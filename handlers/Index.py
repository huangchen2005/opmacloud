# -*- coding:utf-8 -*-
import tornado.web
import logging
from handlers.Basehandler import Basehandler

class IndexHandler(Basehandler):
	def get(self):
		self.render('index.html')
