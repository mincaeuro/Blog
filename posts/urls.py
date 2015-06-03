from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^posts/(?P<post_id>[0-9]+)/', views.detail, name='detail'),
	url(r'^photos/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
]
