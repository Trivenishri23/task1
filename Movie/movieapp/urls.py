from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^movies', Indexview.as_view(), name='index'),
]