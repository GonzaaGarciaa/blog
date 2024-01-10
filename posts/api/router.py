from rest_framework.routers import DefaultRouter
from posts.api.views import PostApiViewSet

routers_post = DefaultRouter()

routers_post.register(prefix='posts', basename='posts', viewset= PostApiViewSet)