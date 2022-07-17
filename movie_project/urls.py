from django.conf.urls import patterns, include, url
from django.contrib import admin
from MovieLib.views import IndexView,CreateView,CreateViewMixin,UpdateView,DeleteView
from Todo import views

from FileSample import views
from django.contrib import messages

# Los siguientes ficheros son para manejar los ficheros subidos al server.!!! 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movie_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^movies/', include('MovieLib.urls')),
    # url(r'^TodoList/', include('Todo.urls')),
    url(r'^SAISA/', include('FileSample.urls')),
	# url(r'^$', include('FileSample.urls')),
	# url(r'^$', IndexView.as_view(), name='movie_index'),
	# url(r'^create$', CreateView.as_view(), name='movie_create'),
	# url(r'^createMixin$', CreateViewMixin.as_view(), name='movie_createMixin'),
	# url(r'^edit/(?P<pk>\d+)$', UpdateView.as_view(), name='movie_edit'),
	# url(r'^delete/(?P<pk>\d+)$', DeleteView.as_view(), name='movie_delete'),
    # url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
    # urlpatterns += patterns('',
        # url(r'^SAISA/(?P<path>.*)$', 'django.views.static.serve', {
            # 'document_root': settings.MEDIA_ROOT,
        # }),
   # )
