import webapp2

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world')

app = webapp2.WSGIApplication([
    ('/', HelloWorld),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()