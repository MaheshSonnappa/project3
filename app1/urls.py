from django.urls import path
from app1.views import *

app_name = "raina"
urlpatterns = [
    path("third/", third, name="third"),
]