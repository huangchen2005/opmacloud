# -*- coding:utf-8 -*-

import torndb
import tornado.web
import os
from config import COOKIE_SECRET, DB_HOST, DB_USER, DB_PASSWD, DB_NAME, DEBUG
from urls import urls

class Connection(torndb.Connection):
	def __init__(self):
        	super(Connection, self).__init__(
			host=DB_HOST, database=DB_NAME,
                        user=DB_USER, password=DB_PASSWD)
        	self._db_args["init_command"] = 'SET time_zone = "+8:00"'
        	try:
            		self.reconnect()
        	except Exception:
            		logging.error("Cannot connect to MySQL on %s", self.host,exc_info=True)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = urls		
        	settings = dict(
            		template_path = os.path.join(os.path.dirname(__file__), "templates"),
            		static_path = os.path.join(os.path.dirname(__file__), "static"),
            		xsrf_cookies = False,
			cookie_secret = COOKIE_SECRET,
			login_url = "/login",
			debug = DEBUG,
		)
        	tornado.web.Application.__init__(self, handlers, **settings)
        	self.db = Connection()
