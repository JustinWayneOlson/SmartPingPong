import tornado.web
import tornado.auth
import json
import os

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
<<<<<<< HEAD
        body = json.loads(self.request.body)
        print "fjkdlsajfkldsa"
        print body
        # TODO update score in firebase
=======
        body = json_decode(self.request.body)
>>>>>>> 902a340... fucking works
        self.write({
            "response": "success"
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
            nextPage = self.get_argument('code')
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
