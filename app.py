import tornado.ioloop
import tornado.autoreload
import os
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('build/index.html')

class TestEndpointHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({'response': 'hello'})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/testEndpoint', TestEndpointHandler),
        (r'/static/js/(.*)',tornado.web.StaticFileHandler, {"path": "./build/static/js"},),
        (r'/static/css/(.*)',tornado.web.StaticFileHandler, {"path": "./build/static/css"},),
        (r'/static/media/(.*)',tornado.web.StaticFileHandler, {"path": "./build/static/media"},)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("serving on port 8888")

    #TODO remove in prod
    tornado.autoreload.start()
    for dir, _, files in os.walk('./'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]

    tornado.ioloop.IOLoop.current().start()
