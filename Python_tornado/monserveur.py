import tornado.httpserver
import tornado.ioloop
import tornado.web
import platform

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		serverinfo=platform.uname()
		self.write("%s" % " ".join(serverinfo))

application=tornado.web.Application([
	(r"/",MainHandler),
	])
if __name__=='__main__':
	http_server=tornado.httpserver.HTTPServer(application)
	http_server.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
	
