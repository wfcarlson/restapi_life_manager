from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^fetch/$', FetchView.as_view()),
    url(r'^link/$', LinkView.as_view())
]
