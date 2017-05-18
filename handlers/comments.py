from google.appengine.api import users

from handlers.base import BaseHandler
from models.comment import Comment
from models.topic import Topic


class AddCommentHandler(BaseHandler):
    def post(self, details_id):
        user = users.get_current_user()

        comment = self.request.get("comment")
        topic = Topic.get_by_id(int(details_id))

        new_comment = Comment(content=comment, author_email=user.email(), topic_id=topic.key.id(), topic_title=topic.title)
        new_comment.put()

        return self.redirect_to("topic-details", details_id=topic.key.id())
