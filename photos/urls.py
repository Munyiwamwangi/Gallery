from django.conf import url
from . import views

url(r"^/$",views.welcome, name="welcome"),
