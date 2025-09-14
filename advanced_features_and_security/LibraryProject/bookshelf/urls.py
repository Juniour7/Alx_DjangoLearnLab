from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('template/', views.template_view),
    path('datetime/', views.current_datetime)
]