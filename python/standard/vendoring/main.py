import webapp2

from google.cloud import datastore


class MainPage(webapp2.RequestHandler):
    def get(self):
        client = datastore.Client()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
