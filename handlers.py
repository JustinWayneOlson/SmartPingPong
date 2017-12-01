import tornado.web
import tornado.auth
import json
import os
from pymongo import MongoClient
from pprint import pprint

def isUserRegistered(db, user_id):
    user = db.users.find_one({ "_id": user_id })
    if user:
        return True
    else:
        return False

def registerUser(db, user):
    newUser = {
        '_id': user['id'],
        'name': ''.join([user['given_name'], ' ', user['family_name']]),
        'avatar': user['picture']
    }
    pprint(newUser)
    users = db['users']
    users.insert(newUser)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        if not self.current_user:
            self.redirect('/auth/login')
            return
        username = tornado.escape.xhtml_escape(self.current_user)
        if not isUserRegistered(self.application.db, json.loads(self.current_user)['id']):
            registerUser(self.application.db, json.loads(self.current_user))
        else:
            print "already registered!"
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
        self.write({
            "response": "success"
        })

class GetScoreHandler(tornado.web.RequestHandler):
    def get(self, match, game):
        score = {"1": 11, "2": 21}
        self.write({
            "response": score
        })

class UpdateTeamHandler(tornado.web.RequestHandler):
    def post(self):
        body = json_decode(self.request.body)
        self.write({
            "reponse": "success"
        })

class GetTeamHandler(tornado.web.RequestHandler):
    def get(self, id):
        team = {"id": id, "name": "Workday Super Owls", "players": ["Jace", "Justin"], "wins": 4, "losses": 0, "rating": 2312, "history": [2, 14, 32, 66]}
        self.write({
            "response": team
        })

class UpdateMatchHandler(tornado.web.RequestHandler):
    def post(self):
        body = json_decode(self.request.body)
        self.write({
            "reponse": "success"
        })

class GetMatchHandler(tornado.web.RequestHandler):
    def get(self, id):
        match = {"id": id, "games": [8, 9, 10], "matchScore": "2-1", "winners": [1, 14], "date": "December 1, 2017"}
        self.write({
            "response": match
        })

class UpdateGameHandler(tornado.web.RequestHandler):
    def post(self):
        body = json_decode(self.request.body)
        self.write({
            "reponse": "success"
        })

class GetGameHandler(tornado.web.RequestHandler):
    def get(self, id):
        game = {"id": id, "players": {"1": [1, 2], "2": [10, 14]}, "scores": {"1": 21, "2": 14}, "winners": [1, 2]}
        self.write({
            "response": match
        })

class ResetGameHandler(tornado.web.RequestHandler):
    def post(self):
        body = json_decode(self.request.body)
        self.write({
            "reponse": "success"
        })

class GoogleOAuth2LoginHandler(tornado.web.RequestHandler, tornado.auth.GoogleOAuth2Mixin):
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument('code', False):
            access = yield self.get_authenticated_user(
                redirect_uri=os.environ['REDIRECT_URI'],
                code=self.get_argument('code'))
            user = yield self.oauth2_request("https://www.googleapis.com/oauth2/v1/userinfo", access_token=access["access_token"])
            self.set_secure_cookie('user', json.dumps(user))
            self.redirect('/')
        else:
            yield self.authorize_redirect(
                redirect_uri=os.environ['REDIRECT_URI'],
                client_id='861279987458-o6v3btjpil2r6rjlm9uro2vddoer3tdh.apps.googleusercontent.com',
                client_secret = "IKuRyyLXrP5sV9iz3lcc-2da",
                scope=['profile', 'email'],
                response_type='code',
                extra_params={'approval_prompt': 'auto'}
            )
