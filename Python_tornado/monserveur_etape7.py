import tornado.httpserver
import tornado.ioloop
import tornado.web
import platform
import datetime


class MainHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		if not self.get_secure_cookie("mycookie"):
			self.set_secure_cookie("mycookie","Whatever you want")
			self.write("Your cookie was not set yet! It should be ok now.\n")
		else:
			self.write("You're using a cookie!!\n")
		serverinfo=platform.uname()
		"""date=datetime.datetime.now()
		date=str(date)
		self.write("\n %s" % " ".join(serverinfo))
		self.write("\n %s" % " ".join(date))"""
		self.render("template.html",pagetitle="\nSystem Information",data=serverinfo)
		self.finish()

class InfoHandler(tornado.web.RequestHandler):
	def get(self,index):
		serverinfo=platform.uname()
		self.write(serverinfo[int(index)])

application=tornado.web.Application([
	(r"/",MainHandler),
	(r"/info/([0-5]+)",InfoHandler),
	],
	cookie_secret="EXJ1io+MoKcuca5KuEq0m1x8+339MDny/CURNQ=")

if __name__=='__main__':
	http_server=tornado.httpserver.HTTPServer(application)
	http_server.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
	
