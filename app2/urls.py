from django.urls import path
from app2.views import *

app_name = "dhoni"
urlpatterns = [
    path("second/", second, name="second"),
]