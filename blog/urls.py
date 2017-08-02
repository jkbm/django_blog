from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),    
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^untitled_unmastered/$', views.post_unpublished, name='post_unpublished'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.post_comment, name='post_comment'),
    url(r'^post/(?P<tag>[\w.-]+)/$', views.post_tags, name = 'post_tag'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

]