from auth.views import *
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^verify/$', verify, name="verify"),
]
