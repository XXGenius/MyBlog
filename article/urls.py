
from django.conf.urls import url

from article.views import articles, article, addlike, addcomment, addarticle, get_category

urlpatterns = [

    url(r'^$', articles),
    
    url(r'^articles/get/(?P<article_id>\d+)/$', article),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', addlike),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', addcomment),

    url(r'^addarticle/$', addarticle),
    url(r'^category/(?P<alias>[^/]+)/', get_category)
    		  ]