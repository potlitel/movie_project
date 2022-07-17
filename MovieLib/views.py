from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404

"Lines for handle messages"
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from MovieLib.models import Movie
from MovieLib.forms import FooForm, MessageMixin

def popup(request):
    template = loader.get_template('FileSampleApp/popup.html')
    context = RequestContext(request, {
        'latest_question_list': "latest_question_list",
    })
    return HttpResponse(template.render(context))   

# Create your views here.
class IndexView(ListView):
	context_object_name = 'car_list'
	template_name = 'index.html'
	model = Movie
	paginate_by = 8  #and that's it !!

class CreateView(MessageMixin,CreateView):
    template_name = 'create.html'
    model = Movie
    success_url = '/'
    success_message = "Created Successfully"
def get_form_kwargs(self):
        """ Add the Request object to the Form's Keyword Arguments. """
        kwargs = super(RequestCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
	
class CreateViewMixin(SuccessMessageMixin, CreateView):
    template_name = 'createMixin.html'
    model = Movie
    form_class = FooForm  # the change is over here
    success_url = '/'
    success_message = "The movie %(title)s was created successfully"
	
class UpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'update.html'
    model = Movie
    success_url = '/'
    success_message = "The movie %(title)s was updated successfully"

class MovieMixin(object):
    model = Movie
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Movie'})
        return kwargs
		
class DeleteView(MovieMixin, DeleteView):
    template_name = 'delete_confirm.html'
    def get_success_url(self):
        return reverse('movie_index')