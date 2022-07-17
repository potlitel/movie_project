from django.conf.urls import patterns, include, url
from django.contrib import admin
from MovieLib import views
from django.contrib import messages

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movie_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^List$', views.IndexView.as_view(), name='movies_index'),
	url(r'^popup$', views.popup, name='popup_index'),
	url(r'^create$', views.CreateView.as_view(), name='movies_create'),
	url(r'^createMixin$', views.CreateViewMixin.as_view(), name='movies_createMixin'),
	url(r'^edit/(?P<pk>\d+)$', views.UpdateView.as_view(), name='movies_edit'),
	url(r'^delete/(?P<pk>\d+)$', views.DeleteView.as_view(), name='movies_delete'),
)
