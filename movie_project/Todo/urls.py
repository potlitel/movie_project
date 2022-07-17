from django.conf.urls import patterns, url
from Todo.views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = patterns('todo.views',
    url(r'^$', TodoList.as_view(), name='todo_list'),
    url(r'^Todo(?P<pk>\d+)$', TodoDetail.as_view(), name='todo_detail'),
    url(r'^New$', TodoCreate.as_view(), name='todo_create'),
    url(r'^Todo(?P<pk>\d+)/Update$', TodoUpdate.as_view(), name='todo_update'),
    url(r'^Todo(?P<pk>\d+)/Delete$', TodoDelete.as_view(), name='todo_delete'),
)