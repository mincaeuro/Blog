from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('posts.urls')),
	
	
]
