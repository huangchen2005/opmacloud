# -*- coding:utf-8 -*-
import tornado.web
import logging
from handlers.Basehandler import Basehandler

class ProblemsHandler(Basehandler):
	def get(self):
		self.render('problems.html')

class ProblemsDomainHandler(Basehandler):
	def get(self):
		self.render('problems_domain.html')

class ProblemsSpaceHandler(Basehandler):
	def get(self):
		self.render('problems_space.html')

class ProblemsProgramHandler(Basehandler):
	def get(self):
		self.render('problems_program.html')

class ProblemsDeploymentHandler(Basehandler):
	def get(self):
		self.render('problems_deployment.html')

class ProblemsOpHandler(Basehandler):
	def get(self):
		self.render('problems_op.html')
