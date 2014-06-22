# -*- coding:utf-8 -*-
import tornado.web
import logging
from handlers.Basehandler import Basehandler

class PriceHandler(Basehandler):
	def get(self):
		self.render('price.html')
