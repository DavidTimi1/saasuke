from django.urls import path
from . import views

app_name = "tg-bot"

urlpatterns = [
    path('', views.index, name="index"),
    path("hook", views.webhook, name="hook"),
]