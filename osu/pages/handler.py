import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello from the OSU Python package!<br>Here is a picture of a penguin:<br><img src="/img/Penguin.jpg">')

class CatchAllHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello from some random URL after /osu/1!')

app = webapp2.WSGIApplication([
	('/osu/1/?', MainHandler),
	('/osu/1.*', CatchAllHandler)
], debug=True)