from django.views.generic.list import ListView
from Todo.models import Todo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Todo.forms import TodoForm,CripsyForm,CripsyFormUpdate
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class TodoList(ListView):
    model = Todo
    template_name = 'TodoApp/todo_list.html'
    context_object_name = 'TodoList'

class TodoDetail(DetailView):
    model = Todo
    template_name = 'TodoApp/details.html'
    @method_decorator(permission_required('todo.view_todo'))
    def dispatch(self, *args, **kwargs):
        return super(TodoDetail, self).dispatch(*args, **kwargs)

class TodoCreate(CreateView):
    model = Todo
    form_class = CripsyForm
    template_name = 'TodoApp/create.html'
    # @method_decorator(permission_required('todo.add_todo'))
    def dispatch(self, *args, **kwargs):
        return super(TodoCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return redirect(self.object)

class TodoUpdate(UpdateView):
    model = Todo
    form_class = CripsyFormUpdate
    template_name = 'TodoApp/create.html'
    @method_decorator(permission_required('todo.change_todo'))
    def dispatch(self, *args, **kwargs):
        return super(TodoUpdate, self).dispatch(*args, **kwargs)

class TodoDelete(DeleteView):
    model = Todo
    template_name = 'TodoApp/delete_confirm.html'
    @method_decorator(permission_required('todo.delete_todo'))
    def dispatch(self, *args, **kwargs):
        return super(TodoDelete, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        # To do this because the success_url class variable isn't reversed...
        return reverse('todo_list')
