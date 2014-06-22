# -*- coding:utf-8 -*-
import tornado.web
import logging
from handlers.Basehandler import Basehandler

class AboutHandler(Basehandler):
	def get(self):
		self.render('about.html')
