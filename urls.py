#-*- coding:utf-8 -*-

from handlers.Index import *
#from handlers.Login import LoginHandler
#from handlers.Login import LogoutHandler
from handlers.Problems import *
from handlers.Features import *
from handlers.Price import *
from handlers.About import *

urls = [
(r'/', IndexHandler),
#(r'/login', LoginHandler),
#(r'/logout', LogoutHandler),
(r'/problems', ProblemsHandler),
(r'/problems/domain', ProblemsDomainHandler),
(r'/problems/space', ProblemsSpaceHandler),
(r'/problems/program', ProblemsProgramHandler),
(r'/problems/deployment', ProblemsDeploymentHandler),
(r'/problems/op', ProblemsOpHandler),
(r'/features', FeaturesHandler),
(r'/features/monitor', FeaturesMonitorHandler),
(r'/features/alarm', FeaturesAlarmHandler),
(r'/features/cdn', FeaturesCDNHandler),
(r'/features/ec', FeaturesEcHandler),
#(r'/features/web_monitor', FeaturesWebMonitorHandler),
#(r'/features/server_monitor', FeaturesServerMonitorHandler),
#(r'/features/service_monitor', FeaturesServiceMonitorHandler),
#(r'/features/alarm', FeaturesAlarmHandler),
#(r'/features/suggest', FeaturesSuggestHandler),
(r'/price', PriceHandler),
(r'/about', AboutHandler),
#(r'/faq', FaqHandler),
]
