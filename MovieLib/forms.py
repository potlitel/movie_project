from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout
from crispy_forms.bootstrap import (FormActions, PrependedText, PrependedAppendedText)
from parsley.decorators import parsleyfy
from MovieLib.models import Movie

class MovieMixin(object):
    model = Movie
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Movie'})
        return kwargs



@parsleyfy		
class FooForm(forms.ModelForm):
    """Model Foo form"""
    class Meta:
        model = Movie

    def __init__(self, *args, **kwargs):
        super(FooForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
             PrependedAppendedText('title','$'),
             PrependedAppendedText('genre','$'),
             PrependedAppendedText('release_date','$'),
             PrependedAppendedText('price','$','.00'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "movie_index" %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            )
            )

class MessageMixin(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)