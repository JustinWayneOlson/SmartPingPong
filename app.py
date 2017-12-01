import tornado.ioloop
import tornado.autoreload
import os
import tornado.web
import handlers
from pymongo import MongoClient

def openMongoConnection():
    client = MongoClient(os.environ['MONGODB_URL'])
    db = client.SmartPingPong
    return db

class Application(tornado.web.Application):
    def __init__(self):
        routes = [
            (r"/", handlers.MainHandler),
            (r'/auth/login', handlers.GoogleOAuth2LoginHandler),
            (r'/getScore/([^\/]*)/(.*)', handlers.GetScoreHandler),
            (r'/updateScore', handlers.UpdateScoreHandler),
            (r'/updateTeam', handlers.UpdateTeamHandler),
            (r'/getTeam/(.*)', handlers.GetTeamHandler),
            (r'/updateMatch', handlers.UpdateMatchHandler),
            (r'/getMatch/(.*)', handlers.GetMatchHandler),
            (r'/updateGame', handlers.UpdateGameHandler),
            (r'/getGame/(.*)', handlers.GetGameHandler),
            (r'/resetGame', handlers.ResetGameHandler),
            # (r'/getGameState/(.*)', handlers.GetGameHandler),
            # (r'/updateGameState', handlers.ResetGameHandler),
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
        super(Application, self).__init__(routes, **settings)

        self.db = openMongoConnection()

if __name__ == "__main__":
    try:
        db = openMongoConnection()
        print "Mongo Connection Opened"
    except:
        print "Unable to establish connection with MongoDB"


    app = Application()
    app.listen(8888)

    #TODO remove in prod
    tornado.autoreload.start()
    for dir, _, files in os.walk('./'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]

    tornado.ioloop.IOLoop.current().start()
    print("Application serving on port 8888")
