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
        scoreUpdate = json.loads(self.request.body)
        #todo save game state (and queue) in memory and fetch scores here
        score = self.application.db.scores.find_one({"": , "": })
        score['1'] += scoreUpdate['team1']
        score['2'] += scoreUpdate['team2']
        self.application.db.scores.(score)
        self.write({
            "response": "success"
        })

class GetScoreHandler(tornado.web.RequestHandler):
    def get(self, match, game):
        score = self.application.db.scores.find_one({"match": match, "game": game})
        self.write({
            "response": score
        })

class UpdateTeamHandler(tornado.web.RequestHandler):
    def post(self):
        team = json_decode(self.request.body)
        self.application.db.teams.insert(team)
        self.write({
            "reponse": "success"
        })

class GetTeamHandler(tornado.web.RequestHandler):
    def get(self, id):
        team = self.application.db.teams.find_one({"_id": id})
        self.write({
            "response": team
        })

class UpdateMatchHandler(tornado.web.RequestHandler):
    def post(self):
        match = json_decode(self.request.body)
        self.application.db.matches.insert(match)
        self.write({
            "reponse": "success"
        })

class GetMatchHandler(tornado.web.RequestHandler):
    def get(self, id):
        match = self.application.db.matches.find_one({"_id": id})
        self.write({
            "response": match
        })

class UpdateGameHandler(tornado.web.RequestHandler):
    def post(self):
        game = json_decode(self.request.body)
        self.application.db.games.insert(game)
        self.write({
            "reponse": "success"
        })

class GetGameHandler(tornado.web.RequestHandler):
    def get(self, id):
        game = self.application.db.games.find_one({"_id": id})
        self.write({
            "response": game
        })

class ResetGameHandler(tornado.web.RequestHandler):
    def post(self):
        body = json_decode(self.request.body)
        self.application.db.games.insert(body)
        self.write({
            "reponse": "success"
        })

# class UpdateGameStateHandler(tornado.web.RequestHandler):
#     def post(self):
#         newGameState = json_decode(self.request.body)
#         self.application.db.gameState.find_one_and_update("_id": }, {"$set": newGameState})
#         self.write({
#             "reponse": "success"
#         })
#
# class GetGameStateHandler(tornado.web.RequestHandler):
#     def get(self):
#         gameState = self.application.db.gameState.find_one()
#         self.write({
#             "response": gameState
#         })

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
