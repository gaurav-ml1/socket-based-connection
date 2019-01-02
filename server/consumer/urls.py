from .views import send_command
from django.urls import re_path

urlpatterns = [
    re_path(r'^send_command/$', send_command)
]