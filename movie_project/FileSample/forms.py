from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div, Field, Fieldset
from crispy_forms.bootstrap import (FormActions, PrependedText, PrependedAppendedText)
from parsley.decorators import parsleyfy
from FileSample.models import (File, Continent, Pais, Publicacion, Evento, PonenciaEvento,
      Capacitacion, Patente, ResultadoIntroducido, Premio, EmpleoEstudiantes, ProyectoiDi,
     Noticia, ModeloYoamel, Ciudad, Membership, TipoObraCientifica, ObraCientifica,
     TamañoObra, NivelAutoria, NivelMES, NivelEvento, TipoPublicacion, TipoCapacitacion,
     RolCapacitación, ModalidadCapacitacion, CienciaObra, TipoObra, TamañoObra, 
     LugarPremio, CaracterPremio, Fuente, CaracterNoticia, NivelProyecto,
     LineaCientificaProyecto, Area, SAI, TipoSAISolicitado, SubTipoSAISolicitado,
     TematicaSAI, PersonalRecibirSAI, TiempoSAI, EvaluacionSAI, Profile, Provincia, Municipio,
     Membresia)
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.utils.translation import ugettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey
from crispy_forms.bootstrap import InlineField, TabHolder, Tab
from FileSample.catalogs import (GENDER, Years, RolProyectoIDi,
     CantidadAutores, CantidadEstudiantes, TiempoVisibilidad, RangoTiempo, NombreFuente)
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.forms.widgets import CheckboxSelectMultiple
from better_filter_widget import BetterFilterWidget
from django.conf import settings

from django.forms.models import formset_factory
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from charsleft_widget.widgets import CharsLeftInput
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.forms.widgets import PasswordInput, TextInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Hidden
from django_password_strength.widgets import PasswordStrengthInput, PasswordConfirmationInput

from passwords.validators import (
        DictionaryValidator, LengthValidator, ComplexityValidator)
from passwords.fields import PasswordField

from related_choice_field.fields import RelatedModelChoiceField

from django_password_strength.widgets import PasswordStrengthInput, PasswordConfirmationInput
from django.db.models import Q

class UserForm1(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required = True, label="Correo electrónico")
    first_name = forms.CharField(required = True, label="Nombre")
    last_name = forms.CharField(required = True, label="Apellidos")
    password1 = forms.CharField(label="Contraseña", widget=PasswordStrengthInput())
    password2 = forms.CharField(label="Confirmar contraseña", widget=PasswordConfirmationInput())
	
    class Meta:
        model = User
        # fields = ('first_name', 'last_name', 'username', 'email', 'password')
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        #exclude = ('password',) 

    def __init__(self, *args, **kwargs):
        super(UserForm1, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("Datos básicos",
              Div(
                Div('first_name',css_class='col-md-6',),
                Div('last_name',css_class='col-md-6',),
                css_class='row',
                ),
              Div(
                Div('username',css_class='col-md-6',),
                Div('email',css_class='col-md-6',),
                css_class='row',
                ),
              Div(
                Div('password1',css_class='col-md-6',),
                Div('password2',css_class='col-md-6',),
                css_class='row',
                ),
            )
            )


class UserEditForm1(forms.ModelForm):
    email = forms.EmailField(required = True, label="Correo electrónico")
    first_name = forms.CharField(required = True, label="Nombre")
    last_name = forms.CharField(required = True, label="Apellidos")
	
    class Meta:
        model = User
        # fields = ('first_name', 'last_name', 'username', 'email', 'password')
        fields = ('first_name', 'last_name', 'username', 'email',)
        exclude = ('password',) 

    def __init__(self, *args, **kwargs):
        super(UserEditForm1, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("Datos básicos",
              Div(
                Div('first_name',css_class='col-md-6',),
                Div('last_name',css_class='col-md-6',),
                css_class='row',
                ),
              Div(
                Div('username',css_class='col-md-6',),
                Div('email',css_class='col-md-6',),
                css_class='row',
                )
            )
            )

class UserProfileForm1(forms.ModelForm):
    provincia = forms.ModelChoiceField(label='Provincia:', queryset=Provincia.objects.all(),to_field_name="id")
    municipio = RelatedModelChoiceField(
        queryset=Municipio.objects.all(),
        related_form_field_name='provincia',
        related_model_name='provincia')
    #anno_graduado = forms.DateField(label='Año de graduado:')
    direccion = forms.CharField(label='Dirección particular:',max_length=255)
    class Meta:
        model = Profile
        fields = (
            'solapin','expediente','sexo','edad','direccion','provincia','municipio',
            'carne_identidad','cargo','categoria_docente','grado_cientifico','especialidad_graduado',
            'anno_graduado','titulo_academico','rol_saisa','grupo',
            )
        widgets = {
            'anno_graduado': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
        }
    def __init__(self, *args, **kwargs):
        super(UserProfileForm1, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TabHolder(
               Tab(
                   'Datos personales',
                   'direccion','provincia','municipio','edad','sexo','carne_identidad',
                   'solapin','expediente'
               ),
               Tab(
                   'Datos profesionales',
                   'categoria_docente','grado_cientifico','especialidad_graduado',
                   'anno_graduado','titulo_academico'
                ),
               Tab(
                   'Rol en SAISA',
                   'cargo','rol_saisa','grupo'
                )
               ),
            # FormActions
            # (
            #     Submit('register', 'Crear usuario SAISA',css_class='span2'),
            # )
            )

























class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        exclude = ('user',)

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # magic 
        # self.user = kwargs['instance'].user
        # user_kwargs = kwargs.copy()
        # user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **kwargs)
        # magic end 

        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)
         
        # define fields order if needed
        self.fields.keyOrder = (
            'last_name',
            'first_name',
            'second_name',

            'solapin',
            'expediente',
            'sexo',

            'edad'
        )

    def save(self, *args, **kwargs):
        # save both forms   
        self.uf.save(*args, **kwargs)
        return super(ProfileForm, self).save(*args, **kwargs)

    class Meta:
        model = Profile

class CustomUserChangeForm( UserChangeForm ):
    def __init__( self, *args, **kwargs ):
        super( CustomUserChangeForm, self ).__init__( *args, **kwargs )
        #if self.instance and self.instance.pk:
            # Since the pk is set this is not a new instance
            #self.fields['username'] = self.instance.username
            #self.fields['username'].widgets.attrs['readonly'] = True

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, label="Correo electrónico")
    first_name = forms.CharField(required = True, label="Nombre")
    last_name = forms.CharField(required = True, label="Apellidos")
    username = forms.CharField(required = True, label="Nombre de usuario")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    # def save(self, commit = True):
    #     user = super(UserCreationForm, self).save(commit = False)
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.password = self.cleaned_data['password1']

    #     if commit:
    #         user.save()

    #     return user

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )
        exclude = ('password',)           
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('username',css_class='span2'),
            Field('first_name',css_class='span2'),
            Field('last_name',css_class='span2'),
            Field('email',css_class='span2'),
            #  FormActions
            # (
            #     Submit('login', 'Actualizar perfil',css_class='span2'),
            # )
            )
    def clean_password(self):
        return ""


class SAISAProfileEditForm(forms.ModelForm):
    provincia = forms.ModelChoiceField(label='Provincia:', queryset=Provincia.objects.all(),to_field_name="id")
    municipio = RelatedModelChoiceField(
        queryset=Municipio.objects.all(),
        related_form_field_name='provincia',
        related_model_name='provincia')
    class Meta:
        model = Profile
        fields = (
            'solapin','expediente','sexo','edad','direccion','provincia','municipio',
            'carne_identidad','cargo','categoria_docente','grado_cientifico','especialidad_graduado',
            'anno_graduado','titulo_academico','rol_saisa','grupo',
            )          
        exclude = ('user',)
        widgets = {
            'anno_graduado': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
            'direccion': forms.Textarea(attrs={'rows':4})
        }
    def __init__(self, *args, **kwargs):
         super(SAISAProfileEditForm, self).__init__(*args, **kwargs)
         self.helper = FormHelper()
         self.helper.form_class = 'form-horizontal'
         self.helper.layout = Layout(
             Div(
                Div('solapin',css_class='col-md-6',),
                Div('expediente',css_class='col-md-6',),
                Div('sexo',css_class='col-md-6',),
                css_class='row',
            ),
             )
    #          FormActions
    #         (
    #             Submit('login', 'Actualizar perfil',css_class='span2'),
    #         )
    #         )
    # def clean_password(self):
    #     return ""        

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(label='Clave de acceso:', widget=PasswordInput())
	# username = forms.CharField(widget=TextInput(attrs={'placeholder': 'escriba un usuario válido'}))
    # password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'y su clave de acceso'}))
    # def __init__(self, *args, **kwargs):
    #     super(MyAuthenticationForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_class = 'form-horizontal'
    #     self.helper.layout = Layout(
    #         Field('username',css_class='span2'),
    #         Field('password',css_class='span2'),
    #          FormActions
    #         (
    #             Submit('login', 'Loginn',css_class='span2'),
    #             Hidden('next', '/IdeaPublisher/')
    #         )
    #         )

class ExampleForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña anterior:',widget=PasswordInput())
    new_password1 = forms.CharField(label='Nueva contraseña:',widget=PasswordStrengthInput())
    new_password2 = forms.CharField(label='Confirmar nueva contraseña:',widget=PasswordConfirmationInput())
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('old_password',css_class='span2'),
            Field('new_password1',css_class='span2'),
            Field('new_password2',css_class='span2'),
            FormActions
            (
                Submit('change', 'Salvar mi nueva clave',css_class='span2'),
            )
        )
        
#from simple_search import BaseSearchForm

class FileMixin(object):
    model = File
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'File'})
        return kwargs

# class MyModelSearchForm(BaseSearchForm):
#     class Meta:
#         base_qs = Publicacion.objects
#         search_fields = ['^propietario','titulo', '@autor', '=id'] 
#         fulltext_indexes = (
#             ('propietario', 2),
#             ('propietario,titulo,autor,id', 1),
#         )

@parsleyfy		
class FileForm(forms.ModelForm):
    item = forms.CharField(help_text="Please enter a username.")
    image = forms.ImageField(widget=forms.FileInput(), help_text="Select a profile image to upload.", required=False)
    File = forms.FileField(help_text="Select a profile image to upload.", required=False)
    anyimage = forms.FileField(help_text="Select a profile image to upload.", required=False)
    # gender = forms.ChoiceField(choices=[('', (u'Select a gender'))])
    gender = forms.ChoiceField(choices=[('', _(u'Select a gender'))] + list(GENDER),widget=forms.Select(attrs={'onchange':'get_vehicle_color();'}))
    name = forms.ChoiceField(widget=forms.Select(), required=False)
    continent = forms.ModelChoiceField(queryset=Continent.objects.all(),to_field_name="id")
    # datetimefiel = forms.DateField(years=range(1950, datetime.date.today().year+50))
    """Model Foo form"""
    class Meta:
        model = File
        fields = ['gender', 'item', 'image', 'File', 'year_in_school', 'anyimage', 'datetimefiel']
        widgets = {
                #Use localization and bootstrap 3
                'datetimefiel': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
            }

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
             'continent',
             'country',
             'gender',
             'name',
             'item',
             'image',
             'File',
             'year_in_school',
             'anyimage',
             'datetimefiel',
             # PrependedAppendedText('item','$'),
             # PrependedAppendedText('image','$'),
             # PrependedAppendedText('File','$'),
             # PrependedAppendedText('year_in_school','$'),
             # PrependedAppendedText('anyimage','$'),
             # PrependedAppendedText('datetimefiel','$'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-big" style="margin-right:5px"
                        href="">Cancel</a>"""),
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


#from smart_selects.form_fields import ChainedModelChoiceField

from django.http import HttpRequest
from django.shortcuts import get_object_or_404

class ObraCientificaForm(forms.ModelForm):
    titulo = forms.CharField(label='Título:',max_length=128)
    tipo_obra = forms.ModelChoiceField(label='Tipo:', queryset=TipoObraCientifica.objects.all(),to_field_name="id")
    #descripcion = forms.CharField(label='Descripción:',max_length=255)
    tamanno = forms.ModelChoiceField(label='Tamaño:', queryset=TamañoObra.objects.all(),to_field_name="id")
    # fecha_creacion = forms.DateField(label='Fecha de creación:')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a esta obra científica.")
    class Meta:
        model = ObraCientifica
        exclude = ('propietario',)
        widgets = {
            'autores': BetterFilterWidget(),
            'fecha_creacion': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows':4}),
        }
        fields = [   
                     'titulo',
                     'tipo_obra',
                     'fecha_creacion',
                     'descripcion',
                     'tamanno',
                     'autores',
                     'fichero',]
        
    class Media:
        css = {'all': ('/static/admin/css/widgets.csss',),}
        # Adding this javascript is crucial
        js = ('/admin/jsi18n',)
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(ObraCientificaForm, self).__init__(*args, **kwargs)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('titulo',css_class='span2'),
             Field('descripcion',css_class='span2'),
             Div(
                Div('tipo_obra',css_class='col-md-6',),
                Div('tamanno',css_class='col-md-6',),
                Div('fecha_creacion',css_class='col-md-6',),
                css_class='row',
            ),
             Field('autores',css_class='span2'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "obras_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear obra científica' if self.is_add else 'Salvar cambios realizados a esta obra científica'),
            )
            )        
class MessageMixinPublicacion(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)


class PublicacionForm(forms.ModelForm):
    # propietario = forms.CharField(initial="{{ User.get_username() }}")
    #propietario = forms.CharField()
    titulo = forms.CharField(label='Título:',max_length=255)
    # autor = forms.ChoiceField(label='Autor:',choices=[('', _(u'Seleccione un autor'))] + list(GENDER))
    # nivel_autoria = forms.ModelChoiceField(label='Nivel de autoría:', queryset=NivelAutoria.objects.all(),to_field_name="id")
    anno = forms.ChoiceField(label='Año:',choices=[('', _(u'Seleccione un año'))] + list(Years))
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a esta publicación.")
    aprobacion = forms.TypedChoiceField(
        label = "Aprobar esta publicación:",
        choices = ((1, "Aprobar"), (0, "No aprobar")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    nivel_mes = forms.ModelChoiceField(label='Nivel MES:', queryset=NivelMES.objects.all(),to_field_name="id")
    class Meta:
        model = Publicacion
        exclude = ('propietario',)
        fields = [   
                     #'propietario',
                     'titulo',
                     'autores',
                     # 'nivel_autoria',
                     'anno',
                     'pais',
                     'ciudad',
                     'editorial',
                     'publicacion',
                     'numero',
                     'volumen',
                     'nivel_mes',
                     'aprobacion',
                     'fichero',]
        widgets = {
            'autores': BetterFilterWidget(),
        }
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PublicacionForm, self).__init__(*args, **kwargs)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             # Field('titulo',css_class='span2'),
             # Field('autor',css_class='span2'),
             Div(
                Div('titulo',css_class='col-md-6',),
                Div('anno',css_class='col-md-6',),
                css_class='row',
            ),
			Field('autores',css_class='span2'),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
            ),
             Field('editorial',css_class='span2'),
             Field('publicacion',css_class='span2'),
             Div(
                Div('numero',css_class='col-md-3',),
                Div('volumen',css_class='col-md-4',),
                Div('nivel_mes',css_class='col-md-5',),
                css_class='row',
            ),
             Field('aprobacion', style="background: #FAFAFA; padding: 10px;",css_class='span2'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "publications_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear publicación' if self.is_add else 'Salvar cambios realizados a esta publicación'),
            )
            )        
class MessageMixinPublicacion(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)



class EventoForm(forms.ModelForm):
    nivel = forms.ModelChoiceField(label='Nivel:', queryset=NivelEvento.objects.all(),to_field_name="id")
    tipo_publicacion = forms.ModelChoiceField(label='Tipo de publicación:', queryset=TipoPublicacion.objects.all(),to_field_name="id")
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    class Meta:
        model = Evento
        fields = [   
                     'nombre',
                     'edicion',
                     'nivel',
                     'pais',
                     'ciudad',
                     'tipo_publicacion',
                     'issn'
                ]
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(EventoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('nombre',css_class='span2'),
             Div(
                Div('edicion',css_class='col-md-6',),
                Div('nivel',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('tipo_publicacion',css_class='col-md-6',),
                Div('issn',css_class='col-md-6',),
                css_class='row',
                ),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "events_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear evento' if self.is_add else 'Salvar cambios realizados a este evento'),
            )
            )        
class MessageMixinEvento(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)


class PonenciaEventoForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    evento = forms.ModelChoiceField(label='Evento:', queryset=Evento.objects.all(),to_field_name="id")
    # nivel_autoria = forms.ModelChoiceField(label='Nivel de autoría:', queryset=NivelAutoria.objects.all(),to_field_name="id")
    # autor = forms.ChoiceField(label='Autor:',choices=[('', _(u'Seleccione un autor'))] + list(GENDER))
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a esta ponencia.")
    class Meta:
        model = PonenciaEvento
        exclude = ('propietario',)
        widgets = {
            'autores': BetterFilterWidget(),
        }
        fields = [   
                     #'propietario',
                     'titulo',
                     'evento',
                     'autores',
                     # 'nivel_autoria',
                     'fichero'
                ]
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PonenciaEventoForm, self).__init__(*args, **kwargs)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Field('titulo',css_class='span2'),
             Field('evento',css_class='span2'),
			 Field('autores',css_class='span2'),
             # Div(
                # Div('autores',css_class='col-md-6',),
                # Div('nivel_autoria',css_class='col-md-6',),
                # css_class='row',
                # ),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "ponencia_eventos_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear ponencia' if self.is_add else 'Salvar cambios realizados a esta ponencia'),
            )
            )        
class MessageMixinPonenciaEvento(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)

class ArticleForm(forms.Form):
     title = forms.CharField()
     pub_date = forms.DateField()

from django.contrib import admin
class MembershipInline(forms.ModelForm):
    model = Membership
    extra = 1

from crispy_extensions.forms import ModelFormWithFormsets
from crispy_extensions.helper import FormsetContainer
from crispy_extensions.layout import InlineFormSet

class EmploymentContainer(FormsetContainer):
    """Save the employment form(s)"""
    def save(self, boundformset, instance):
        for form in boundformset:
            if form.is_bound and form.changed_data and not form.errors:
                # Form has been filled in, has changed since instantiation
                # and contains no errors
                obj = form.save(commit=False)
                obj.contact = instance
                obj.save()
				
from django.forms.models import modelformset_factory				

class MembresiaForm(forms.ModelForm):
    class Meta:
        model = Membresia
        exclude = ('proyectoIDi',)

MAX_INGREDIENTS = 5

IngredientFormSet = modelformset_factory(Membresia,
    MembresiaForm,
    can_delete=True,
    extra=0)

class ProyectoIDiForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    nivel = forms.ModelChoiceField(label='Nivel:', queryset=NivelProyecto.objects.all(),to_field_name="id")
    linea_cientifica = forms.ModelChoiceField(label='Linea científica:', queryset=LineaCientificaProyecto.objects.all(),to_field_name="id")
    area_ejecutora = forms.ModelChoiceField(label='Area Ejecutora:', queryset=Area.objects.all(),to_field_name="id")
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este proyecto I+D+i.")
    class Meta:
        model = ProyectoiDi
        exclude = ('propietario',)
        widgets = {
            'miembros': BetterFilterWidget(),
        }
        fields = [   
                    #'propietario',
                     'titulo',
                     'nivel',
                     'area_ejecutora',
                     'linea_cientifica',
                     'fichero',
                     'miembros',
                ]
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(ProyectoIDiForm, self).__init__(*args, **kwargs)
        self.fields['miembros'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['miembros'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Field('titulo',css_class='span2'),
             Div(
                Div('nivel',css_class='col-md-6',),
                Div('area_ejecutora',css_class='col-md-6',),
                css_class='row',
                ),
             Field('linea_cientifica',css_class='span2'),
             Field('fichero',css_class='span2'),
             Fieldset("Conformar membresia",
                'miembros'
             ),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="">Cancelar</a>"""),
                Submit('save', 'Crear proyecto Idi' if self.is_add else 'Salvar cambios realizados a este proyecto'),
            )
            )

class CapacitacionForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    tipo = forms.ModelChoiceField(label='Tipo:', queryset=TipoCapacitacion.objects.all(),to_field_name="id")
    rol = forms.ModelChoiceField(label='Rol:', queryset=RolCapacitación.objects.all(),to_field_name="id")
    modalidad = forms.ModelChoiceField(label='Modalidad:', queryset=ModalidadCapacitacion.objects.all(),to_field_name="id")
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a esta capacitación.")
    class Meta:
        model = Capacitacion
        exclude = ('propietario',)
        fields = [   
                     #'propietario',
                     'nombre',
                     'tipo',
                     'fecha',
                     'rol',
                     'modalidad',
                     'institucion',
                     'pais',
                     'ciudad',
                     'fichero',
                     'estudiantes',
                     'profesores'
                ]
        widgets = {
                #Use localization and bootstrap 3
                'fecha': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                'estudiantes': BetterFilterWidget(),
                'profesores': BetterFilterWidget(),
            }        
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(CapacitacionForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].queryset = User.objects.filter(perfil__cargo=10).prefetch_related('perfil')
        self.fields['estudiantes'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.fields['profesores'].queryset = User.objects.filter(perfil__cargo=1).prefetch_related('perfil')
        self.fields['profesores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Field('nombre',css_class='span2'),
             Div(
                Div('tipo',css_class='col-md-6',),
                Div('fecha',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('rol',css_class='col-md-6',),
                Div('modalidad',css_class='col-md-6',),
                css_class='row',
                ),
             Field('institucion',css_class='span2'),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
                ),
             Field('fichero',css_class='span2'),
             # Field('estudiantes',css_class='col-md-6'),
             # Field('profesores',css_class='col-md-6'),
             TabHolder(
               Tab(
                   'Seleccionar estudiantes',
                   'estudiantes',
               ),
               Tab(
                   'Seleccionar profesores',
                   'profesores',
                )),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "capacitacion_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear capacitación' if self.is_add else 'Salvar cambios realizados a esta capacitación'),
            )
            )                            
class MessageMixinCapacitacion(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)



class PatenteForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    ciencia_obra = forms.ModelChoiceField(label='Ciencia de la obra:', queryset=CienciaObra.objects.all(),to_field_name="id")
    tipo_obra = forms.ModelChoiceField(label='Tipo de obra:', queryset=TipoObraCientifica.objects.all(),to_field_name="id")
    cantidad_autores = forms.ChoiceField(label='Cantidad de autores:', choices=[('', _(u'Seleccione cantidad de autores'))] + list(CantidadAutores))    
    #comentario = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows':4, 'cols':60})), 
    #comentario = forms.CharField(widget=SummernoteInplaceWidget())
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a esta patente.")
    class Meta:
        model = Patente
        exclude = ('propietario',)
        fields = [   
                     #'propietario',
                     'nombre_obra',
                     'ciencia_obra',
                     'fecha',
                     'tipo_obra',
                     'fuente_registro',
                     'cantidad_autores',
					 'propietarios',
                     'comentario',
                     'fichero'
                ]
        widgets = {
                #Use localization and bootstrap 3
                'propietarios': BetterFilterWidget(),
                'fecha': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                'comentario': forms.Textarea(attrs={'rows':4}),
            }        
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PatenteForm, self).__init__(*args, **kwargs)
        self.fields['propietarios'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['propietarios'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Field('nombre_obra',css_class='span2'),
             Div(
                Div('ciencia_obra',css_class='col-md-6',),
                Div('fecha',css_class='col-md-6',),
                css_class='row',
                ),
             Field('tipo_obra',css_class='span2'),
             Div(
                Div('fuente_registro',css_class='col-md-6',),
                Div('cantidad_autores',css_class='col-md-6',),
                css_class='row',
                ),
			 Field('propietarios', rows="5"),
             Field('comentario', rows="5"),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "patente_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear patente' if self.is_add else 'Salvar cambios realizados a esta patente'),
            )
            )                            
class MessageMixinPatente(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)


class ResultadoIntroducidoForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    ciencia_obra = forms.ModelChoiceField(label='Ciencia de la obra:', queryset=CienciaObra.objects.all(),to_field_name="id")
    tipo_obra = forms.ModelChoiceField(label='Tipo de obra:', queryset=TipoObraCientifica.objects.all(),to_field_name="id")  
    tamanno = forms.ModelChoiceField(label='Tamaño:', queryset=TamañoObra.objects.all(),to_field_name="id")
    cantidad_autores = forms.ChoiceField(label='Cantidad de autores:', choices=[('', _(u'Seleccione cantidad de autores'))] + list(CantidadAutores))    
    # comentario = forms.CharField(widget = forms.Textarea()), 
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este resultado introducido.")
    class Meta:
        model = ResultadoIntroducido
        exclude = ('propietario',)
        fields = [   
                     #'propietario',
                     'nombre_obra',
                     'ciencia_obra',
                     'fecha',
                     'tamanno',
                     'tipo_obra',
                     'institucion',
                     'cantidad_autores',
                     'comentario',
                     'fichero'
                ]
        widgets = {
                #Use localization and bootstrap 3
                'fecha': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                'comentario': forms.Textarea(attrs={'rows':4})
            }        
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(ResultadoIntroducidoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Field('nombre_obra',css_class='span2'),
             Div(
                Div('ciencia_obra',css_class='col-md-6',),
                Div('fecha',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('tipo_obra',css_class='col-md-6',),
                Div('tamanno',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('institucion',css_class='col-md-7',),
                Div('cantidad_autores',css_class='col-md-5',),
                css_class='row',
                ),
             Field('comentario', rows="5"),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "resultadointroducido_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear resultado' if self.is_add else 'Salvar cambios realizados a este resultado'),
            )
            )                            


class PremioForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    # nivel_autoria = forms.ModelChoiceField(label='Nivel de autoría:', queryset=NivelAutoria.objects.all(),to_field_name="id")
    anno = forms.ChoiceField(label='Año:',choices=[('', _(u'Seleccione un año'))] + list(Years))
    lugar_premio = forms.ModelChoiceField(label='Lugar:', queryset=LugarPremio.objects.all(),to_field_name="id")  
    nivel_premio = forms.ModelChoiceField(label='Nivel:', queryset=NivelEvento.objects.all(),to_field_name="id")
    caracter = forms.ModelChoiceField(label='Caracter:', queryset=CaracterPremio.objects.all(),to_field_name="id")
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este premio.")
    class Meta:
        model = Premio
        exclude = ('propietario',)
        widgets = {
            'autores': BetterFilterWidget(),
        }
        fields = [   
                     #'propietario',
                     'titulo',
                     'autores',
                     # 'nivel_autoria',
                     'anno',
                     'pais',
                     'ciudad',
                     'lugar_premio',
                     'nivel_premio',
                     'caracter',
                     'fichero'
                ]
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PremioForm, self).__init__(*args, **kwargs)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Field('titulo',css_class='span2'),
			 Field('anno',css_class='col-md-6',),
             Field('autores',css_class='span2'),
             # Div(
                # Div('nivel_autoria',css_class='col-md-6',),
                # Div('anno',css_class='col-md-6',),
                # css_class='row',
                # ),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('lugar_premio',css_class='col-md-4',),
                Div('nivel_premio',css_class='col-md-4',),
                Div('caracter',css_class='col-md-4',),
                css_class='row',
                ),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "premio_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear premio' if self.is_add else 'Salvar cambios realizados a este premio'),
            )
            )                            
			
class PremioPublicacionForm(forms.ModelForm):
    anno = forms.ChoiceField(label='Año:',choices=[('', _(u'Seleccione un año'))] + list(Years))
    lugar_premio = forms.ModelChoiceField(label='Lugar:', queryset=LugarPremio.objects.all(),to_field_name="id")  
    nivel_premio = forms.ModelChoiceField(label='Nivel:', queryset=NivelEvento.objects.all(),to_field_name="id")
    caracter = forms.ModelChoiceField(label='Caracter:', queryset=CaracterPremio.objects.all(),to_field_name="id")
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este premio.")
    class Meta:
        model = Premio
        exclude = ('propietario','ponenciaevento', 'proyecto', 'obracientifica')
        widgets = {
            'autores': BetterFilterWidget(),
        }
        fields = [   
                     'titulo',
                     'autores',
                     'publicacion',
                     'anno',
                     'pais',
                     'ciudad',
                     'lugar_premio',
                     'nivel_premio',
                     'caracter',
                     'fichero'
                ]
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PremioPublicacionForm, self).__init__(*args, **kwargs)
        self.fields['publicacion'].queryset = Publicacion.objects.filter(aprobacion=1)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('titulo',css_class='span2'),
             Field('autores',css_class='span2'),
             Div(
                Div('publicacion',css_class='col-md-6',),
                Div('anno',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('lugar_premio',css_class='col-md-4',),
                Div('nivel_premio',css_class='col-md-4',),
                Div('caracter',css_class='col-md-4',),
                css_class='row',
                ),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "premio_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear premio' if self.is_add else 'Salvar cambios realizados a este premio'),
            )
            )			
			
class PremioPonenciaForm(forms.ModelForm):
    anno = forms.ChoiceField(label='Año:',choices=[('', _(u'Seleccione un año'))] + list(Years))
    lugar_premio = forms.ModelChoiceField(label='Lugar:', queryset=LugarPremio.objects.all(),to_field_name="id")  
    nivel_premio = forms.ModelChoiceField(label='Nivel:', queryset=NivelEvento.objects.all(),to_field_name="id")
    caracter = forms.ModelChoiceField(label='Caracter:', queryset=CaracterPremio.objects.all(),to_field_name="id")
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este premio.")
    class Meta:
        model = Premio
        exclude = ('propietario','publicacion', 'proyecto', 'obracientifica')
        widgets = {
            'autores': BetterFilterWidget(),
        }
        fields = [   
                     'titulo',
                     'autores',
                     'ponenciaevento',
                     'anno',
                     'pais',
                     'ciudad',
                     'lugar_premio',
                     'nivel_premio',
                     'caracter',
                     'fichero'
                ]
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PremioPonenciaForm, self).__init__(*args, **kwargs)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('titulo',css_class='span2'),
             Field('autores',css_class='span2'),
             Div(
                Div('ponenciaevento',css_class='col-md-6',),
                Div('anno',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('lugar_premio',css_class='col-md-4',),
                Div('nivel_premio',css_class='col-md-4',),
                Div('caracter',css_class='col-md-4',),
                css_class='row',
                ),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "premio_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear premio' if self.is_add else 'Salvar cambios realizados a este premio'),
            )
            )			
			
			
class PremioProyectoForm(forms.ModelForm):
    anno = forms.ChoiceField(label='Año:',choices=[('', _(u'Seleccione un año'))] + list(Years))
    lugar_premio = forms.ModelChoiceField(label='Lugar:', queryset=LugarPremio.objects.all(),to_field_name="id")  
    nivel_premio = forms.ModelChoiceField(label='Nivel:', queryset=NivelEvento.objects.all(),to_field_name="id")
    caracter = forms.ModelChoiceField(label='Caracter:', queryset=CaracterPremio.objects.all(),to_field_name="id")
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este premio.")
    class Meta:
        model = Premio
        exclude = ('propietario','publicacion', 'ponenciaevento', 'obracientifica')
        widgets = {
            'autores': BetterFilterWidget(),
        }
        fields = [   
                     'titulo',
                     'autores',
                     'proyecto',
                     'anno',
                     'pais',
                     'ciudad',
                     'lugar_premio',
                     'nivel_premio',
                     'caracter',
                     'fichero'
                ]
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PremioProyectoForm, self).__init__(*args, **kwargs)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('titulo',css_class='span2'),
             Field('autores',css_class='span2'),
             Div(
                Div('proyecto',css_class='col-md-6',),
                Div('anno',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('lugar_premio',css_class='col-md-4',),
                Div('nivel_premio',css_class='col-md-4',),
                Div('caracter',css_class='col-md-4',),
                css_class='row',
                ),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "premio_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear premio' if self.is_add else 'Salvar cambios realizados a este premio'),
            )
            )						

class PremioObraForm(forms.ModelForm):
    anno = forms.ChoiceField(label='Año:',choices=[('', _(u'Seleccione un año'))] + list(Years))
    lugar_premio = forms.ModelChoiceField(label='Lugar:', queryset=LugarPremio.objects.all(),to_field_name="id")  
    nivel_premio = forms.ModelChoiceField(label='Nivel:', queryset=NivelEvento.objects.all(),to_field_name="id")
    caracter = forms.ModelChoiceField(label='Caracter:', queryset=CaracterPremio.objects.all(),to_field_name="id")
    pais = forms.ModelChoiceField(label='País:', queryset=Pais.objects.all(),to_field_name="id")
    ciudad = RelatedModelChoiceField(
        queryset=Ciudad.objects.all(),
        related_form_field_name='pais',
        related_model_name='pais')
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este premio.")
    class Meta:
        model = Premio
        exclude = ('propietario','publicacion', 'ponenciaevento', 'proyecto')
        widgets = {
            'autores': BetterFilterWidget(),
        }
        fields = [   
                     'titulo',
                     'autores',
                     'obracientifica',
                     'anno',
                     'pais',
                     'ciudad',
                     'lugar_premio',
                     'nivel_premio',
                     'caracter',
                     'fichero'
                ]
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(PremioObraForm, self).__init__(*args, **kwargs)
        self.fields['autores'].queryset = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        self.fields['autores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('titulo',css_class='span2'),
             Field('autores',css_class='span2'),
             Div(
                Div('obracientifica',css_class='col-md-6',),
                Div('anno',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('pais',css_class='col-md-6',),
                Div('ciudad',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('lugar_premio',css_class='col-md-4',),
                Div('nivel_premio',css_class='col-md-4',),
                Div('caracter',css_class='col-md-4',),
                css_class='row',
                ),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "premio_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear premio' if self.is_add else 'Salvar cambios realizados a este premio'),
            )
            )									
			

class EmpleoEstudiantesForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    fuente = forms.ModelChoiceField(label='Fuente:', queryset=Fuente.objects.all(),to_field_name="id")
    nombre_fuente = forms.ChoiceField(label='Nombre de la Fuente:', choices=[('', _(u'Seleccione una fuente'))] + list(NombreFuente))    
    nombre_obra = forms.ModelChoiceField(label='Nombre de obra:', queryset=ObraCientifica.objects.all(),to_field_name="id")  
    cantidad_estudiantes = forms.ChoiceField(label='Cantidad de estudiantes:', choices=[('', _(u'Seleccione una cantidad'))] + list(CantidadEstudiantes))    
    #estudiantes = forms.ModelMultipleChoiceField(User.objects.all(),widget=FilteredSelectMultiple("Usuarios",False,attrs={'rows':'2'}))
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este empleo de estudiantes.")
    class Meta:
        model = EmpleoEstudiantes
        exclude = ('propietario',)
        widgets = {
            'estudiantes': BetterFilterWidget(),
        }
        fields = [   
                     #'propietario',
                     'fuente',
                     'nombre_fuente',
                     'nombre_obra',
                     'cantidad_estudiantes',
                     'estudiantes',
                     'fichero'
                ]
    class Media:
        css = {'all': ('/static/admin/css/widgets.csss',),}
        # Adding this javascript is crucial
        js = ('/admin/jsi18n',)

    # def save(self, commit=True):
    #     instance = super(EmpleoEstudiantesForm, self).save(commit=False)
    #     if self.propietario:
    #         instance.propietario = self.propietario
    #     return intance.save()    

    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        self.request = kwargs.pop("request", False)
        # self.propietario = kwargs.pop("propietario", False)
        # self.fields["propietario"].queryset = kwargs.pop("propietario", False)
        super(EmpleoEstudiantesForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].queryset = User.objects.filter(perfil__cargo=10)
        self.fields['estudiantes'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        # self.fields["propietario"] = self.request.user
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Div(
                Div('fuente',css_class='col-md-6',),
                Div('nombre_fuente',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('nombre_obra',css_class='col-md-6',),
                Div('cantidad_estudiantes',css_class='col-md-6',),
                css_class='row',
                ),
             Field('estudiantes',css_class='col-md-6'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="{% url "empleoestudiantes_index" %}">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "empleoestudiantes_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear empleo' if self.is_add else 'Salvar cambios realizados a este empleo'),
            )
            )

class EmpleoEstudiantesPublicacionForm(forms.ModelForm):  
    cantidad_estudiantes = forms.ChoiceField(label='Cantidad de estudiantes:', choices=[('', _(u'Seleccione una cantidad'))] + list(CantidadEstudiantes))    
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este empleo de estudiantes.")
    class Meta:
        model = EmpleoEstudiantes
        exclude = ('propietario','ponenciaevento','proyecto','obracientifica',)
        widgets = {
            'estudiantes': BetterFilterWidget(),
        }
        fields = [   
                     'publicacion',
                     'cantidad_estudiantes',
                     'estudiantes',
                     'fichero'
                ]
    class Media:
        css = {'all': ('/static/admin/css/widgets.csss',),}
        # Adding this javascript is crucial
        js = ('/admin/jsi18n',)    

    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        self.request = kwargs.pop("request", False)
        super(EmpleoEstudiantesPublicacionForm, self).__init__(*args, **kwargs)
        self.fields["publicacion"].queryset = Publicacion.objects.filter(aprobacion=1)
        self.fields['estudiantes'].queryset = User.objects.filter(perfil__cargo=10)
        self.fields['estudiantes'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('publicacion',css_class='col-md-6'),
			 # Div(
                # Div('fuente',css_class='col-md-6',),
                # Div('nombre_fuente',css_class='col-md-6',),
                # css_class='row',
                # ),
             Field('cantidad_estudiantes',css_class='col-md-6'),	
             Field('estudiantes',css_class='col-md-6'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "empleoestudiantes_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear empleo' if self.is_add else 'Salvar cambios realizados a este empleo'),
            )
            )			
			
class EmpleoEstudiantesPonenciaForm(forms.ModelForm):
    cantidad_estudiantes = forms.ChoiceField(label='Cantidad de estudiantes:', choices=[('', _(u'Seleccione una cantidad'))] + list(CantidadEstudiantes))    
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este empleo de estudiantes.")
    class Meta:
        model = EmpleoEstudiantes
        exclude = ('propietario','publicacion','proyecto','obracientifica',)
        widgets = {
            'estudiantes': BetterFilterWidget(),
        }
        fields = [   
                     'ponenciaevento',
                     'cantidad_estudiantes',
                     'estudiantes',
                     'fichero'
                ]
    class Media:
        css = {'all': ('/static/admin/css/widgets.csss',),}
        # Adding this javascript is crucial
        js = ('/admin/jsi18n',)    

    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        self.request = kwargs.pop("request", False)
        super(EmpleoEstudiantesPonenciaForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].queryset = User.objects.filter(perfil__cargo=10)
        self.fields['estudiantes'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('ponenciaevento',css_class='col-md-6'),
			 # Div(
                # Div('fuente',css_class='col-md-6',),
                # Div('nombre_fuente',css_class='col-md-6',),
                # css_class='row',
                # ),
             Field('cantidad_estudiantes',css_class='col-md-6'),	
             Field('estudiantes',css_class='col-md-6'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "empleoestudiantes_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear empleo' if self.is_add else 'Salvar cambios realizados a este empleo'),
            )
            )						

class EmpleoEstudiantesProyectoForm(forms.ModelForm):
    cantidad_estudiantes = forms.ChoiceField(label='Cantidad de estudiantes:', choices=[('', _(u'Seleccione una cantidad'))] + list(CantidadEstudiantes))    
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este empleo de estudiantes.")
    class Meta:
        model = EmpleoEstudiantes
        exclude = ('propietario','publicacion','ponenciaevento','obracientifica',)
        widgets = {
            'estudiantes': BetterFilterWidget(),
        }
        fields = [   
                     'proyecto',
                     'cantidad_estudiantes',
                     'estudiantes',
                     'fichero'
                ]
    class Media:
        css = {'all': ('/static/admin/css/widgets.csss',),}
        # Adding this javascript is crucial
        js = ('/admin/jsi18n',)    

    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        self.request = kwargs.pop("request", False)
        super(EmpleoEstudiantesProyectoForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].queryset = User.objects.filter(perfil__cargo=10)
        self.fields['estudiantes'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('proyecto',css_class='col-md-6'),
			 # Div(
                # Div('fuente',css_class='col-md-6',),
                # Div('nombre_fuente',css_class='col-md-6',),
                # css_class='row',
                # ),
             Field('cantidad_estudiantes',css_class='col-md-6'),	
             Field('estudiantes',css_class='col-md-6'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "empleoestudiantes_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear empleo' if self.is_add else 'Salvar cambios realizados a este empleo'),
            )
            )									
			
class EmpleoEstudiantesObraForm(forms.ModelForm):
    cantidad_estudiantes = forms.ChoiceField(label='Cantidad de estudiantes:', choices=[('', _(u'Seleccione una cantidad'))] + list(CantidadEstudiantes))    
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a este empleo de estudiantes.")
    class Meta:
        model = EmpleoEstudiantes
        exclude = ('propietario','publicacion','ponenciaevento','proyecto',)
        widgets = {
            'estudiantes': BetterFilterWidget(),
        }
        fields = [   
                     'obracientifica',
                     'cantidad_estudiantes',
                     'estudiantes',
                     'fichero'
                ]
    class Media:
        css = {'all': ('/static/admin/css/widgets.csss',),}
        # Adding this javascript is crucial
        js = ('/admin/jsi18n',)    

    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        self.request = kwargs.pop("request", False)
        super(EmpleoEstudiantesObraForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].queryset = User.objects.filter(perfil__cargo=10)
        self.fields['estudiantes'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('obracientifica',css_class='col-md-6'),
			 # Div(
                # Div('fuente',css_class='col-md-6',),
                # Div('nombre_fuente',css_class='col-md-6',),
                # css_class='row',
                # ),
             Field('cantidad_estudiantes',css_class='col-md-6'),	
             Field('estudiantes',css_class='col-md-6'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "empleoestudiantes_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear empleo' if self.is_add else 'Salvar cambios realizados a este empleo'),
            )
            )			

	
class NoticiaForm(forms.ModelForm):
    #propietario = forms.CharField(initial = settings.AUTH_USER_MODEL)
    rango_tiempo = forms.ChoiceField(label='Rango de Tiempo:', choices=[('', _(u'Seleccione'))] + list(RangoTiempo))
    tiempo_visibilidad = forms.ChoiceField(label='Tiempo de visibilidad:', choices=[('', _(u'Seleccione'))] + list(TiempoVisibilidad))    
    caracter = forms.ModelChoiceField(label='Caracter:', queryset=CaracterNoticia.objects.all(),to_field_name="id")
    aprobacion = forms.TypedChoiceField(
        label = "Aprobar esta noticia:",
        choices = ((1, "Aprobar"), (0, "No aprobar")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    fichero = forms.FileField(label='Fichero asociado:',help_text="<strong>Nota:</strong> Seleccione un fichero para asociar a esta noticia.")
    class Meta:
        model = Noticia
        exclude = ('propietario',)
        fields = [   
                     #'propietario',
                     'titular',
                     'rango_tiempo',
                     'publicacion',
                     'tiempo_visibilidad',
                     'caracter',
                     'contenido',
                     'aprobacion',
                     'fichero'
                ]
        widgets = {
                #Use localization and bootstrap 3
                'publicacion': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                'contenido': forms.Textarea(attrs={'rows':4})
            }
        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             #Field('propietario',css_class='span2',readonly=True),
             Field('titular',css_class='span2'),
             Div(
                Div('rango_tiempo',css_class='col-md-6',),
                Div('publicacion',css_class='col-md-6',),
                css_class='row',
                ),
             Div(
                Div('tiempo_visibilidad',css_class='col-md-6',),
                Div('caracter',css_class='col-md-6',),
                css_class='row',
                ),
             Field('contenido',css_class='span2'),
             Field('aprobacion',css_class='span2'),
             Field('fichero',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "noticia_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear noticia' if self.is_add else 'Salvar cambios realizados a esta noticia'),
            )
            )                                        


class SAIForm(forms.ModelForm):
    area_solicitante = forms.CharField(max_length=255)
    codigo = forms.CharField(label='Código:',max_length=255)
    tipo_SAI = forms.ModelChoiceField(label='Tipo SAI:', queryset=TipoSAISolicitado.objects.all(),to_field_name="id")
    subtipo_SAI = RelatedModelChoiceField(label='Subtipo SAI:',
        queryset=SubTipoSAISolicitado.objects.all(),
        related_form_field_name='tipo_SAI',
        related_model_name='tipo')
    personal_SAI = forms.ModelChoiceField(label='Cantidad de personas a recibir el servicio solicitado:', queryset=PersonalRecibirSAI.objects.all(),to_field_name="id")
    tematica_SAI = forms.ModelChoiceField(label='Temática del servicio solicitado:', queryset=TematicaSAI.objects.all(),to_field_name="id")
    tiempo_SAI = forms.ModelChoiceField(label='Tiempo estimado de duración del servicio solicitado:', queryset=TiempoSAI.objects.all(),to_field_name="id")
    class Meta:
        model = SAI
        exclude = ('aprobacion','aprobador_SAI','aprobador_cargo_SAI','responsable_ejecucion_SAI',
        'comentario_SAI_No_Aprobacion','evaluacion_SAI','comentario_SAI_evaluacion',)
        fields = [ 
                     'area_solicitante',
                     'codigo',
					 'nombre_solicitante',
					 'cargo_solicitante',
					 'solapin_solicitante',
					 'email_solicitante',
                     'tipo_SAI',
                     'subtipo_SAI',
                     'personal_SAI',
                     'tematica_SAI',
                     'tiempo_SAI',
                     'ejecutores',
                     'fecha',
                     'descripcion_SAI',
                 ]
        widgets = {
                #Use localization and bootstrap 3
                'ejecutores': BetterFilterWidget(),
                'fecha': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                'descripcion_SAI': forms.Textarea(attrs={'rows':4}),
            }        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(SAIForm, self).__init__(*args, **kwargs)
        self.fields['ejecutores'].queryset = User.objects.all()
        self.fields['ejecutores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('area_solicitante',css_class='span2'),
             Div(
                Div('fecha',css_class='col-md-6',),
                Div('codigo',css_class='col-md-6',),
                css_class='row',
            ),
			Fieldset("Datos del solicitante",
             Div(
                Div('nombre_solicitante',css_class='col-md-6',),
                Div('cargo_solicitante',css_class='col-md-6',),
                css_class='row',
            ),
			Div(
                Div('solapin_solicitante',css_class='col-md-6',),
                Div('email_solicitante',css_class='col-md-6',),
                css_class='row',
            )
			),
            Fieldset("Datos del servicio a solicitar",
             Div(
                Div('tipo_SAI',css_class='col-md-6',),
                Div('subtipo_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div('personal_SAI',css_class='col-md-6',),
                Div('tematica_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div('tiempo_SAI',css_class='col-md-6',),
                Div('descripcion_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Field('ejecutores',css_class='span2'),
            ),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "sais_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear SAI' if self.is_add else 'Salvar cambios realizados a este SAI'),
            )
            )     


class SAIAprobacionForm(forms.ModelForm):
    area_solicitante = forms.CharField(max_length=255)
    codigo = forms.CharField(label='Código:',max_length=255)
    tipo_SAI = forms.ModelChoiceField(label='Tipo SAI:', queryset=TipoSAISolicitado.objects.all(),to_field_name="id")
    subtipo_SAI = RelatedModelChoiceField(label='Subtipo SAI:',
        queryset=SubTipoSAISolicitado.objects.all(),
        related_form_field_name='tipo_SAI',
        related_model_name='tipo')
    personal_SAI = forms.ModelChoiceField(label='Cantidad de personas a recibir el servicio solicitado:', queryset=PersonalRecibirSAI.objects.all(),to_field_name="id")
    tematica_SAI = forms.ModelChoiceField(label='Temática del servicio solicitado:', queryset=TematicaSAI.objects.all(),to_field_name="id")
    tiempo_SAI = forms.ModelChoiceField(label='Tiempo estimado de duración del servicio solicitado:', queryset=TiempoSAI.objects.all(),to_field_name="id")
    aprobacion = forms.TypedChoiceField(
        label = "Aprobar este servicio:",
        choices = ((1, "Aprobado"), (0, "No aprobado")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    class Meta:
        model = SAI
        exclude = ('nombre_solicitante','cargo_solicitante','solapin_solicitante','telefono_solicitante',
        'email_solicitante','evaluacion_SAI','comentario_SAI_evaluacion',)
        fields = [ 
                     'area_solicitante',
                     'codigo',
                     'tipo_SAI',
                     'subtipo_SAI',
                     'personal_SAI',
                     'tematica_SAI',
                     'tiempo_SAI',
                     'ejecutores',
                     'fecha',
                     'descripcion_SAI',
                     'aprobacion',
                     #'aprobador_SAI',
                     'aprobador_cargo_SAI',
                     'responsable_ejecucion_SAI',
                     'comentario_SAI_No_Aprobacion'
                 ]
        widgets = {
                #Use localization and bootstrap 3
                'ejecutores': BetterFilterWidget(),
                'fecha': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                'descripcion_SAI': forms.Textarea(attrs={'rows':4}),
                'comentario_SAI_No_Aprobacion': forms.Textarea(attrs={'rows':4}),
            }        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(SAIAprobacionForm, self).__init__(*args, **kwargs)
        # without the next line label_from_instance does NOT work
        self.fields['responsable_ejecucion_SAI'].queryset = User.objects.all()
        self.fields['responsable_ejecucion_SAI'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.fields['ejecutores'].queryset = User.objects.all()
        self.fields['ejecutores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('area_solicitante',css_class='span2'),
             Div(
                Div('fecha',css_class='col-md-6',),
                Div('codigo',css_class='col-md-6',),
                css_class='row',
            ),
            Fieldset("Datos del servicio a solicitar",
             Div(
                Div('tipo_SAI',css_class='col-md-6',),
                Div('subtipo_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div('personal_SAI',css_class='col-md-6',),
                Div('tematica_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div('tiempo_SAI',css_class='col-md-6',),
                Div('descripcion_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Field('ejecutores',css_class='span2'),
            ),
            Fieldset("Aprobación",
                Div(
                Div('aprobacion',css_class='col-md-6',),
                Div('responsable_ejecucion_SAI',css_class='col-md-6',),
                css_class='row',
            ),
                Div(
                Div('aprobador_cargo_SAI',css_class='col-md-6',),
                Div('comentario_SAI_No_Aprobacion',css_class='col-md-6',),
                css_class='row',
            ),
            ),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "sais_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear SAI' if self.is_add else 'Salvar cambios realizados a este SAI'),
            )
            )     


class SAIEvaluacionForm(forms.ModelForm):
    area_solicitante = forms.CharField(max_length=255)
    codigo = forms.CharField(label='Código:',max_length=255)
    tipo_SAI = forms.ModelChoiceField(label='Tipo SAI:', queryset=TipoSAISolicitado.objects.all(),to_field_name="id")
    subtipo_SAI = RelatedModelChoiceField(label='Subtipo SAI:',
        queryset=SubTipoSAISolicitado.objects.all(),
        related_form_field_name='tipo_SAI',
        related_model_name='tipo')
    personal_SAI = forms.ModelChoiceField(label='Cantidad de personas a recibir el servicio solicitado:', queryset=PersonalRecibirSAI.objects.all(),to_field_name="id")
    tematica_SAI = forms.ModelChoiceField(label='Temática del servicio solicitado:', queryset=TematicaSAI.objects.all(),to_field_name="id")
    tiempo_SAI = forms.ModelChoiceField(label='Tiempo estimado de duración del servicio solicitado:', queryset=TiempoSAI.objects.all(),to_field_name="id")
    class Meta:
        model = SAI
        exclude = ('nombre_solicitante','cargo_solicitante','solapin_solicitante','telefono_solicitante',
        'email_solicitante','aprobacion','aprobador_SAI','aprobador_cargo_SAI','responsable_ejecucion_SAI',
        'comentario_SAI_No_Aprobacion')
        fields = [ 
                     'area_solicitante',
                     'codigo',
                     'tipo_SAI',
                     'subtipo_SAI',
                     'personal_SAI',
                     'tematica_SAI',
                     'tiempo_SAI',
                     'ejecutores',
                     'fecha',
                     'descripcion_SAI',
                     'evaluacion_SAI',
                     'comentario_SAI_evaluacion'
                 ]
        widgets = {
                #Use localization and bootstrap 3
                'ejecutores': BetterFilterWidget(),
                'fecha': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                'descripcion_SAI': forms.Textarea(attrs={'rows':4}),
                'comentario_SAI_evaluacion': forms.Textarea(attrs={'rows':4}),
            }        
    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop("is_add", False)
        super(SAIEvaluacionForm, self).__init__(*args, **kwargs)
        self.fields['ejecutores'].queryset = User.objects.all()
        self.fields['ejecutores'].label_from_instance = lambda obj: "%s %s"% (obj.first_name, obj.last_name)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('area_solicitante',css_class='span2'),
             Div(
                Div('fecha',css_class='col-md-6',),
                Div('codigo',css_class='col-md-6',),
                css_class='row',
            ),
            Fieldset("Datos del servicio a solicitar",
             Div(
                Div('tipo_SAI',css_class='col-md-6',),
                Div('subtipo_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div('personal_SAI',css_class='col-md-6',),
                Div('tematica_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Div(
                Div('tiempo_SAI',css_class='col-md-6',),
                Div('descripcion_SAI',css_class='col-md-6',),
                css_class='row',
            ),
            Field('ejecutores',css_class='span2'),
            ),
            Fieldset("Evaluación",
                Div(
                Div('evaluacion_SAI',css_class='col-md-6',),
                Div('comentario_SAI_evaluacion',css_class='col-md-6',),
                css_class='row',
            )
            ),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="{% url "sais_index" %}">Cancelar</a>"""),
                Submit('save', 'Crear SAI' if self.is_add else 'Salvar cambios realizados a este SAI'),
            )
            )

class ModeloYoamelForm(forms.ModelForm):
    href = forms.CharField(label='href (Relacionado con):')
    data_largesrc = forms.FileField(label='data_largesrc (Imagen grande):',help_text="<strong>Nota:</strong> Imagen grande.")
    data_title = forms.CharField(label='data_title (Titulo):')
    img = forms.FileField(label='Img (Imagen pequeña):',help_text="<strong>Nota:</strong> Imagen pequeña.")
    class Meta:
        model = ModeloYoamel
        fields = [   
                     'href',
                     'data_largesrc',
                     'data_title',
                     'data_description',
                     'img'
                ]
        widgets = {
                'data_description': forms.Textarea(attrs={'rows':4})
            }
        
    def __init__(self, *args, **kwargs):
        super(ModeloYoamelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
             Field('data_title',css_class='span2'),
             Field('data_description',css_class='span2'),
             Field('data_largesrc',css_class='span2'),
             Field('img',css_class='span2'),
             Field('href',css_class='span2'),
             FormActions
            (
                # HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        # href="">Vista previa</a>"""),
                HTML("""<a role="button" class="btn btn-default" style="margin-right:5px"
                        href="">Cancelar</a>"""),
                Submit('save', 'Crear'),
            )
            ) 
			
class MessageMixinYoamelForm(object):
    """
    Make it easy to display notification messages when using Class Based Views.
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)    
