from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'posts', views.PostView, basename='post')
router.register(r'comments', views.CommentView, basename='comment') # this endpoint still needs work

urlpatterns = [
   path('', include(router.urls)),
   path('feed/', views.Feed.as_view(), name='user-feed'),
]