import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    # serves index.html
    def get(self):
        self.render('./build/index.html')

class UpdateScoreHandler(tornado.web.RequestHandler):
    # POST endpoint
    # Expected body
    # {
    #   team: int,
    #   delta: +/- 1
    # }
    # returns {response: "success"}
    def post(self):
        body = json.loads(self.request.body)
        print "fjkdlsajfkldsa"
        print body
        # TODO update score in firebase
        self.write({
            "response": "success"
        })
