
from django.conf.urls import url
from django.contrib import admin



from loginsys.views import login, logout , register , changeuser, acc
urlpatterns = [

    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    url(r'^usersettings/$', changeuser),
    url(r'^acc/$', acc)
]