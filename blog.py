"""
    This is the main module.
    It's responsible for setup global variables,
    routes and associate them with its handlers.
"""
import common.request as request
import webapp2
from config import config
from handlers.home import EditPostHandler
from handlers.home import CommentHandler
from handlers.home import LikeHandler
from handlers.home import NewPostHandler
from handlers.home import PostHandler
from handlers.home import WelcomeHandler
from handlers.login.login import SignIn
from handlers.login.login import SignOut
from handlers.login.login import SignUp

config.jinja_env = request.load_templates(
    __file__,
    ['handlers/login/views', 'handlers/views']
)
request.BlogHandler.login_page = '/blog/signin'

app = webapp2.WSGIApplication([
    ('/blog/signup', SignUp),
    (request.BlogHandler.login_page, SignIn),
    ('/blog/logout', SignOut),
    (r'/blog/?', WelcomeHandler),
    (r'/?', WelcomeHandler),
    ('/blog/newpost', NewPostHandler),
    webapp2.Route(r'/blog/<post_id:\d+>/like',
                  LikeHandler,
                  name='like'),
    webapp2.Route(r'/blog/<post_id:\d+>',
                  PostHandler,
                  name='post_detail'),
    webapp2.Route(r'/blog/edit/<post_id:\d+>',
                  EditPostHandler,
                  name='edit_post'),
    webapp2.Route(r'/blog/<post_id:\d+>/comment',
                  CommentHandler,
                  name='comment'),
    webapp2.Route(r'/blog/<post_id:\d+>/comment/<comment_id:\d+>',
                  CommentHandler,
                  name='edit_comment')
], debug=True)
