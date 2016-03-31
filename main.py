##
# Code from the video, provided by Justin Wolford
##

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world')

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)