# -*- coding:utf-8 -*-
import tornado.web
import logging
from handlers.Basehandler import Basehandler

class FeaturesHandler(Basehandler):
	def get(self):
		self.render('features.html')

class FeaturesMonitorHandler(Basehandler):
	def get(self):
		self.render('features_monitor.html')

class FeaturesAlarmHandler(Basehandler):
	def get(self):
		self.render('features_alarm.html')

class FeaturesCDNHandler(Basehandler):
	def get(self):
		self.render('features_cdn.html')

class FeaturesEcHandler(Basehandler):
	def get(self):
		self.render('features_ec.html')
