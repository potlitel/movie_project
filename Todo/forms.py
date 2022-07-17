from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import (FormActions, PrependedText, PrependedAppendedText)
from Todo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'priority', 'due_on',)

class CripsyForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'priority')

        # helper = FormHelper()
        # helper.form_class = 'form-horizontal'
        # helper.label_class = 'col-lg-2'
        # helper.field_class = 'col-lg-8'
        # helper.layout = Layout(
        #         Field('title', css_class='input-xlarge'),
        #         Field('priority', css_class='input-xlarge'),
        #         FormActions
        #         (
        #             HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
        #                     href="{% url "todo_list" %}">Cancel</a>"""),
        #             Submit('save', 'Save this todo'),
        #         )
        #         )    
        #fields = ('title', 'priority')

    def __init__(self, *args, **kwargs):
        super(CripsyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_class = 'form-inline'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
             # PrependedAppendedText('title','$'),
             # PrependedAppendedText('priority'),
            # 'title',
            # 'priority',
            Field('title', css_class='input-xlarge'),
            Field('priority', css_class='input-xlarge'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "todo_list" %}">Cancel</a>"""),
                Submit('save', 'Save this todo'),
            )
            )

class CripsyFormUpdate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'priority', 'due_on',)

    def __init__(self, *args, **kwargs):
        super(CripsyFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
             PrependedAppendedText('title','$'),
             PrependedAppendedText('priority'),
             PrependedAppendedText('due_on','$'),

             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "todo_list" %}">Cancel</a>"""),
                Submit('save', 'Update this todo'),
            )
            )