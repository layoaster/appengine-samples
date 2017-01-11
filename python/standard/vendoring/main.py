import webapp2

from google.cloud import bigquery


class MainPage(webapp2.RequestHandler):
    def get(self):
        client = bigquery.Client()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
