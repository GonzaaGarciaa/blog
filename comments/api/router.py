from rest_framework.routers import DefaultRouter
from comments.api.views import CommentApiViewSet


routers_comment = DefaultRouter()

routers_comment.register(prefix='comments', basename='comments', viewset=CommentApiViewSet)