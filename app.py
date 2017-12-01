import tornado.ioloop
import tornado.autoreload
import os
import tornado.web
import handlers

def make_app():

    routes = [
        (r"/", handlers.MainHandler),
        (r"/user/(.*)"
        (r'/auth/login', handlers.GoogleOAuth2LoginHandler),
        (r'/updateScore', handlers.UpdateScoreHandler),
        (r'/static/js/(.*)', tornado.web.StaticFileHandler, {"path": "./build/static/js"},),
        (r'/static/css/(.*)', tornado.web.StaticFileHandler, {"path": "./build/static/css"},),
        (r'/static/media/(.*)', tornado.web.StaticFileHandler, {"path": "./build/static/media"},)
    ]

    settings = {
        'google_oauth' : {
            'key': os.environ['OAUTH_CLIENT_ID'],
            'secret': os.environ['OAUTH_CLIENT_SECRET'],
        },
        'redirect_uri': os.environ['REDIRECT_URI'],
        'login_url': 'auth/login',
        'cookie_secret': os.urandom(32),
    }
    return tornado.web.Application(routes, **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("serving on port 8888")

    #TODO remove in prod
    tornado.autoreload.start()
    for dir, _, files in os.walk('./'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]

    tornado.ioloop.IOLoop.current().start()
