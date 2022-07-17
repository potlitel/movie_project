from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from FileSample.models import (File, Publicacion, Evento, PonenciaEvento, ProyectoiDi,
     Capacitacion, Patente, ResultadoIntroducido, Premio, EmpleoEstudiantes, Noticia, 
     ModeloYoamel, Membership, ObraCientifica, SAI, Profile, Membresia)
from FileSample.forms import (FileForm, PublicacionForm, EventoForm, PonenciaEventoForm, 
     ProyectoIDiForm, CapacitacionForm, PatenteForm, ResultadoIntroducidoForm, PremioForm, 
	 PremioPublicacionForm, PremioPonenciaForm, PremioProyectoForm, PremioObraForm, EmpleoEstudiantesForm, EmpleoEstudiantesPublicacionForm, EmpleoEstudiantesPonenciaForm, EmpleoEstudiantesProyectoForm, EmpleoEstudiantesObraForm, NoticiaForm, ModeloYoamelForm, CustomUserChangeForm, UserEditForm,
     SAISAProfileEditForm, ObraCientificaForm, SAIForm, SAIAprobacionForm, SAIEvaluacionForm, 
     MyRegistrationForm, ProfileForm, UserForm1, UserEditForm1, UserProfileForm1, MembresiaForm, IngredientFormSet)
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from phantom_pdf import render_to_pdf
from django.http import HttpResponse
from django.core.urlresolvers import resolve, reverse_lazy
from django.utils.six.moves.urllib.parse import urlparse

import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.http import StreamingHttpResponse

from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet
from django.contrib import admin

def submit_recipe(request):
    def get_success_url(self):
        return reverse('inicio')
    if request.method == 'POST':

        form = ProyectoIDiForm(data=request.POST)
        ingredient_formset = IngredientFormSet(data=request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            if ingredient_formset.is_valid():
                recipe.propietario = request.user
                recipe.save()
                ingredient_formset.save()
                recipe.save_m2m()
                return HttpResponseRedirect(self.get_success_url())
    else:
        form = ProyectoIDiForm()
        ingredient_formset = IngredientFormSet()
		
    return render_to_response("recipes/submit.html", 
		{"form": form, "ingredient_formset": ingredient_formset}, context_instance=RequestContext(request))

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm1(data=request.POST)
        profile_form = UserProfileForm1(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            # user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        #endif
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm1()
        profile_form = UserProfileForm1()

    # Render the template depending on the context.
    return render_to_response(
            'Registration/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

class UserMixin(object):
    model = User
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'User'})
        return kwargs
class UserDeleteView(UserMixin, DeleteView):
    template_name = 'FileSampleApp/Userdelete_confirm.html'
    def get_success_url(self):
        return reverse('users_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(*args, **kwargs)




















# class ItemInline(InlineFormSet):
#     model = User

# class CreateOrderView(CreateWithInlinesView):
#     model = Profile
#     inlines = ItemInline    
#     form_class = SAISAProfileEditForm
#     template_name = 'FileSampleApp/ProyectoIDiCreateMixin.html'

class AlainCreate(SuccessMessageMixin, CreateView):
    template_name = 'accounts/teacher_form1.html'
    model = Profile
    form_class = ProfileForm 
    success_message = "El usuario '%(username)s' ha sido creado con éxito" 
    def get_success_url(self):
        return reverse('sais_index')
    def get_object(self, queryset=None):
         return self.request.user.id
        # return get_object_or_404(User, pk=1)
    # def get_form_kwargs(self):
    #     kwargs = super(AlainCreate, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user.id
    #     return kwargs

# def handler404(request):
#     response = render_to_response('Exceptions/404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response

# ##
# # Handle 404 Errors
# # @param request WSGIRequest list with all HTTP Request
# def error404(request):
#     # 1. Load models for this view
#     #from idgsupply.models import My404Method
#     # 2. Generate Content for this view
#     # template = loader.get_template('404.htm')
#     template_name = 'Exceptions/404.html'   
#     context = Context({
#         'message': 'All: %s' % request,
#         })
#     # 3. Return Template for this view + Data
#     return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

class InicioView(TemplateView):
    template_name = 'CICE/Inicio.html'   

class ContactosView(TemplateView):
    template_name = 'CICE/Contactos.html'   

class InvestigadoresView(TemplateView):
    template_name = 'CICE/Investigadores.html' 
	
class CalendarView(TemplateView):
    template_name = 'CICE/Calendar.html' 	

class TeacherCreation(SuccessMessageMixin, CreateView):
    """
    Creates new teacher
    """
    template_name = 'accounts/teacher_form.html'
    form_class = SAISAProfileEditForm
    model = Profile
    second_form_class = MyRegistrationForm
    success_message = 'Teacher profile saved successfully'
    def get_success_url(self):
        return reverse('file_index')
    def get_context_data(self, **kwargs):
        context = super(TeacherCreation, self).get_context_data(**kwargs)
        context['user_form'] = self.second_form_class
        return context
    def form_valid(self, form):
        user_form = MyRegistrationForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            teacher = form.save(commit=False)
            teacher.user_id = user.id
            teacher.save()
        return HttpResponseRedirect(self.get_success_url())

class TeacherUpdate(SuccessMessageMixin, UpdateView):
    """
    Update teacher profile
    """
    template_name = 'accounts/teacher_form.html'
    model = User
    form_class = UserEditForm1
    second_form_class = UserProfileForm1
    success_message = 'Teacher profile saved successfully'
 
    def get_context_data(self, **kwargs):
        context = super(TeacherUpdate, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.request.user)
        context['user_form'] = self.second_form_class( instance=self.request.user.perfil)
        return context
    # def get(self, request, *args, **kwargs):
         # super(TeacherUpdate, self).get(request, *args, **kwargs)
         # form = self.form_class
         # user_form = self.second_form_class
         # return self.render_to_response(self.get_context_data(
             # object=self.request.user, form=form, form2=user_form))
    def form_valid(self, form):
        user_form = UserProfileForm1(self.request.POST, instance=self.request.user.perfil)
        if user_form.is_valid():
            user_form.save(commit=False)
            user_form.user_id = self.request.user
            user_form.save()
        else:
            return self.render_to_response(self.get_context_data(form=self.form_class, user_form=self.second_form_class))	
        return super(TeacherUpdate, self).form_valid(form)
    # def save(self, *args, **kwargs):
        # u = self.instance.user
        # u.first_name = self.cleaned_data['first_name']
        # u.last_name = self.cleaned_data['last_name']
        # u.email = self.cleaned_data['email']
        # u.save()
        # profile = super(UserProfileForm1, self).save(*args,**kwargs)
        # return profile
    # def save(self, *args, **kwargs):
        # # save both forms   
        # self.form_class.save(*args, **kwargs)
        # return super(UserProfileForm1, self).save(*args, **kwargs)
        # user = super(UserEditForm1, self).save(commit=True)
        # user_profile = UserProfileForm1(user=user)
        # user_profile.save()
        # return user, user_profile
    # def form_valid(self, form):
        # user_form = self.form_class(data=self.request.POST)
        # profile_form = self.second_form_class(data=self.request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
            # user_form.save()
            # profile_form.save(commit=False)
            # profile_form.user_id = user_form.id
            # profile_form.save()
        # return super(TeacherUpdate, self).form_valid(form)
        # return HttpResponseRedirect(self.get_success_url())
    # def form_invalid(self, **kwargs):
        # return self.render_to_response(self.get_context_data(**kwargs))		
    # def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        # form = self.form_class(request.POST)
        # form2 = self.second_form_class(request.POST)
        # return HttpResponseRedirect(self.get_success_url())
        # if form.is_valid() and form2.is_valid():
            # form.save()
			# # used to set the password, but no longer necesarry
            # employeedata = form2.save(commit=False)
            # employeedata.user_id = form
            # employeedata.save()
            # return HttpResponseRedirect(self.get_success_url())
        # else:
            # return self.render_to_response(
            # self.get_context_data(form=form, form2=form2))
    def get_object(self, queryset=None):
        return self.request.user
        # return get_object_or_404(User, pk=1)
    def get_success_url(self):
        return reverse('inicio')


class UsuarioUpdate(SuccessMessageMixin, UpdateView):
    """
    Update teacher profile
    """
    template_name = 'accounts/teacher_form.html'
    model = User
    form_class = UserEditForm1
    second_form_class = UserProfileForm1
    success_message = 'Teacher profile saved successfully'
 
    def get_context_data(self, **kwargs):
        context = super(UsuarioUpdate, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.object)
        context['user_form'] = self.second_form_class( instance=self.object.perfil)
        return context
    def form_valid(self, form):
        user_form = UserProfileForm1(self.request.POST, instance=self.object.perfil)
        if user_form.is_valid():
            user_form.save(commit=False)
            user_form.user_id = self.request.user
            user_form.save()
        else:
            return self.render_to_response(self.get_context_data(form=self.form_class, user_form=self.second_form_class))	
        return super(UsuarioUpdate, self).form_valid(form)
    def get_success_url(self):
        return reverse('inicio')		
		

class UserEdit(UpdateView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('file_index')
    template_name = 'accounts/settings.html'
 
    def get_object(self, queryset=None):
        return self.request.user

@login_required
def editar_perfil(request):

    if request.method == 'POST':
        # formulario enviado
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = SAISAProfileEditForm(request.POST, instance=request.user)

        if user_form.is_valid() and perfil_form.is_valid():
            # formulario validado correctamente
            user_form.save()
            perfil_form.save()
            return HttpResponseRedirect('file_index')
    else:
        # formulario inicial
        user_form = UserEditForm(instance=request.user)
        perfil_form = SAISAProfileEditForm(instance=request.user)

    return render_to_response('accounts/editar_perfil.html', { 'user_form': user_form,  'perfil_form': perfil_form }, context_instance=RequestContext(request))

def alain(request):
    if request.user.is_authenticated(self):
        # Do something for logged-in users.
        return user.get_full_name()        

@login_required 
def settings( request, template_name = 'accounts/settings.html' ):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    page_title = 'Account Settings'
    if request.method == 'POST':
        form = UserEditForm(instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm()
    title = 'Settings'
    return render_to_response( template_name, locals(), context_instance = RequestContext( request) )

@csrf_exempt
def get_sectors(request):
    response = []
    industry_id = int(request.POST['id_pais'])

    # With the sector_id you know wich sector the user has selected
    # You should generate the list based in your needs
    data = []
    if industry_id:
        sectors = INDUSTRY_DICT[industry_id]  # This return a list of ID's of sectors
        # Then make loop over all sectors
        for sector_id in sectors:  
            # To get the sector name you should use another dict
            # I think you already have it in USER_PROFILE_CURRENT_SECTOR_TYPES
            # Remember to import it (check above)
            sector_name =  USER_PROFILE_CURRENT_SECTOR_TYPES[sector_id]
            # We append the id and the name to replace options in the HTML
            data.append({'id':sector_id, 'name':sector_name})  

        response = { 'item_list':data }  # We send back the list
        return HttpResponse(simplejson.dumps(response))

    # If we get any error, or cannot get the sector, we send an empty response
    response = {}
    return HttpResponse(simplejson.dumps(response))

# Create your views here.
class FileCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/createMixin.html'
    model = File
    form_class = FileForm  # the change is over here
    success_url = '/'
    success_message = "The item %(item)s was created successfully"

class FileListView(ListView):
	context_object_name = 'items_list'
	template_name = 'FileSampleApp/List.html'
	model = File
	# paginate_by = 8    

class FileItemMixin(object):
    model = File
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'File'})
        return kwargs
		
class DeleteView(FileItemMixin, DeleteView):
    template_name = 'FileSampleApp/delete_confirm.html'
    def get_success_url(self):
        return reverse('file_index')    

# SAISA APP GENERIC LIST VIEWS
class PublicationsListView(ListView):
    context_object_name = 'publications'
    template_name = 'FileSampleApp/PublicationsListView.html'
    model = Publicacion
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return Publicacion.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PublicationsListView, self).dispatch(*args, **kwargs)

class EventsListView(ListView):
    context_object_name = 'events'
    template_name = 'FileSampleApp/EventsListView.html'
    model = Evento
	
class UsersListView(ListView):
    context_object_name = 'users'
    template_name = 'FileSampleApp/UsuariosListView.html'
    model = User
    #paginate_by = 4
    def get_queryset(self):
        return User.objects.exclude(username="admin")
		#Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')

class PonenciaEventoListView(ListView):
    context_object_name = 'ponencia_eventos'
    template_name = 'FileSampleApp/PonenciaEventoListView.html'
    model = PonenciaEvento
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return PonenciaEvento.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PonenciaEventoListView, self).dispatch(*args, **kwargs)

class CapacitacionListView(ListView):
    context_object_name = 'capacitaciones'
    template_name = 'FileSampleApp/CapacitacionListView.html'
    model = Capacitacion
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return Capacitacion.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacitacionListView, self).dispatch(*args, **kwargs)

class PatenteListView(ListView):
    context_object_name = 'patentes'
    template_name = 'FileSampleApp/PatenteListView.html'
    model = Patente
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return Patente.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PatenteListView, self).dispatch(*args, **kwargs)

class ProyectoIDiListView(ListView):
    context_object_name = 'proyectosIDi'
    template_name = 'FileSampleApp/ProyectoIDiListView.html'
    model = ProyectoiDi
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return ProyectoiDi.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProyectoIDiListView, self).dispatch(*args, **kwargs)

class EmpleoEstudiantesListView(ListView):
    context_object_name = 'empleoestudiantes'
    template_name = 'FileSampleApp/EmpleoEstudiantesListView.html'
    model = EmpleoEstudiantes
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return EmpleoEstudiantes.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesListView, self).dispatch(*args, **kwargs)

class ResultadoIntroducidoListView(ListView):
    context_object_name = 'resultados_introducidos'
    template_name = 'FileSampleApp/ResultadoIntroducidoListView.html'
    model = ResultadoIntroducido
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return ResultadoIntroducido.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultadoIntroducidoListView, self).dispatch(*args, **kwargs)

class PremioListView(ListView):
    context_object_name = 'premios'
    template_name = 'FileSampleApp/PremioListView.html'
    model = Premio
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return Premio.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioListView, self).dispatch(*args, **kwargs)

class NoticiaToWorkerListView(ListView):
    context_object_name = 'news'
    template_name = 'Noticias/noticias.html'
    model = Noticia
    def get_queryset(self):
        return Noticia.objects.filter(aprobacion=1)	
	
class NoticiaListView(ListView):
    context_object_name = 'noticias'
    #queryset = FilebabyFile.objects.order_by('-id')
    template_name = 'FileSampleApp/NoticiaListView.html'
    model = Noticia
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return Noticia.objects.filter(propietario_id=self.propietario.id)

class ObraCientificaListView(ListView):
    context_object_name = 'obras'
    #queryset = FilebabyFile.objects.order_by('-id')
    template_name = 'FileSampleApp/ObraCientificaListView.html'
    model = ObraCientifica
    def get_queryset(self):
        self.propietario = get_object_or_404(User, username=self.request.user)
        return ObraCientifica.objects.filter(propietario_id=self.propietario.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObraCientificaListView, self).dispatch(*args, **kwargs)

class SAIListView(ListView):
    context_object_name = 'sais'
    #queryset = FilebabyFile.objects.order_by('-id')
    template_name = 'FileSampleApp/SAIListView.html'
    model = SAI
    def get_queryset(self):
        self.solicitante = get_object_or_404(User, username=self.request.user)
        return SAI.objects.filter(solicitante_id=self.solicitante.id)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SAIListView, self).dispatch(*args, **kwargs)

# SAISA APP GENERIC CREATE VIEWS
class SAICreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/SAICreateMixin.html'
    model = SAI
    form_class = SAIForm 
    success_message = "El SAI solicitado '%(area_solicitante)s' ha sido creado con éxito" 
    def get_success_url(self):
        return reverse('sais_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(SAICreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SAICreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.solicitante = self.request.user
        obj.aprobacion = 0
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())
class SAIUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/SAIUpdate.html'
    model = SAI
    form_class = SAIForm 
    success_message = "El SAI solicitado '%(area_solicitante)s' ha sido editado con éxito" 
    def get_success_url(self):
        return reverse('sais_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SAIUpdateView, self).dispatch(*args, **kwargs)
class SAIUpdateAprobacionView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/SAIUpdateAprobacion.html'
    model = SAI
    form_class = SAIAprobacionForm 
    success_message = "El SAI solicitado '%(area_solicitante)s' ha sido editado con éxito" 
    def get_success_url(self):
        return reverse('sais_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SAIUpdateAprobacionView, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.aprobador_SAI = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())
class SAIUpdateEvaluacionView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/SAIUpdateEvaluacion.html'
    model = SAI
    form_class = SAIEvaluacionForm 
    success_message = "El SAI solicitado '%(area_solicitante)s' ha sido editado con éxito" 
    def get_success_url(self):
        return reverse('sais_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SAIUpdateEvaluacionView, self).dispatch(*args, **kwargs)
class SAIMixin(object):
    model = SAI
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'SAI'})
        return kwargs
class SAIDeleteView(SAIMixin, DeleteView):
    template_name = 'FileSampleApp/SAIdelete_confirm.html'
    def get_success_url(self):
        return reverse('sais_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SAIDeleteView, self).dispatch(*args, **kwargs)
class SAIDetailView(DetailView):
    template_name = 'FileSampleApp/SAIDetails.html'
    model = SAI        



class ObraCientificaCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/ObraCientificaCreateMixin.html'
    model = ObraCientifica
    form_class = ObraCientificaForm 
    success_message = "La obra científica '%(titulo)s' ha sido creada con éxito" 
    def get_success_url(self):
        return reverse('obras_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(ObraCientificaCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        # kwargs['user'] = {{ User.get_username(self) }}
        return kwargs
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObraCientificaCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class ObraCientificaUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/ObraCientificaUpdate.html'
    model = ObraCientifica
    form_class = ObraCientificaForm 
    success_message = "La obra científica '%(titulo)s' ha sido editada con éxito" 
    def get_success_url(self):
        return reverse('obras_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObraCientificaUpdateView, self).dispatch(*args, **kwargs)
class ObraCientificaMixin(object):
    model = ObraCientifica
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'ObraCientifica'})
        return kwargs
class ObraCientificaDeleteView(ObraCientificaMixin, DeleteView):
    template_name = 'FileSampleApp/ObraCientificadelete_confirm.html'
    def get_success_url(self):
        return reverse('obras_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ObraCientificaDeleteView, self).dispatch(*args, **kwargs)
class ObraCientificaDetailView(DetailView):
    template_name = 'FileSampleApp/ObraCientificaDetails.html'
    model = ObraCientifica        


class PublicacionCreate(SuccessMessageMixin, CreateView):
    coding= "utf-8"
    template_name = 'FileSampleApp/PublicacionCreateMixin.html'
    model = Publicacion
    form_class = PublicacionForm 
    success_message = "La publicación '%(titulo)s' ha sido creada con éxito" 
    def get_success_url(self):
        return reverse('publications_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PublicacionCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        # kwargs['user'] = {{ User.get_username(self) }}
        return kwargs
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PublicacionCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class PublicacionUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/PublicationUpdate.html'
    model = Publicacion
    form_class = PublicacionForm 
    success_message = "La publicación '%(titulo)s' ha sido editada con éxito" 
    def get_success_url(self):
        return reverse('publications_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PublicacionUpdateView, self).dispatch(*args, **kwargs)
class PublicacionMixin(object):
    model = Publicacion
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Publicacion'})
        return kwargs
class PublicacionDeleteView(PublicacionMixin, DeleteView):
    template_name = 'FileSampleApp/Publicaciondelete_confirm.html'
    def get_success_url(self):
        return reverse('publications_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PublicacionDeleteView, self).dispatch(*args, **kwargs)
class PublicacionDetailView(DetailView):
    template_name = 'FileSampleApp/PublicacionDetails.html'
    model = Publicacion
		

class EventoCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/EventoCreateMixin.html'
    model = Evento
    form_class = EventoForm 
    success_message = "El evento '%(nombre)s' ha sido creado con éxito"            
    def get_success_url(self):
        return reverse('events_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(EventoCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventoCreate, self).dispatch(*args, **kwargs)   
class EventoUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/EventUpdate.html'
    model = Evento
    form_class = EventoForm 
    success_message = "El evento '%(nombre)s' ha sido editado con éxito"
    def get_success_url(self):
        return reverse('events_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventoUpdateView, self).dispatch(*args, **kwargs)
class EventoMixin(object):
    model = Evento
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Evento'})
        return kwargs
class EventoDeleteView(EventoMixin, DeleteView):
    template_name = 'FileSampleApp/Eventodelete_confirm.html'
    def get_success_url(self):
        return reverse('events_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventoDeleteView, self).dispatch(*args, **kwargs)
class EventoDetailView(DetailView):
    template_name = 'FileSampleApp/EventoDetails.html'
    model = Evento
	

class PonenciaEventoCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/PonenciaEventoCreateMixin.html'
    model = PonenciaEvento
    form_class = PonenciaEventoForm 
    success_message = "La ponencia en evento '%(titulo)s' ha sido creada con éxito"   
    def get_success_url(self):
        return reverse('ponencia_eventos_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PonenciaEventoCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs      
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PonenciaEventoCreate, self).dispatch(*args, **kwargs)  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class PonenciaEventoUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/PonenciaUpdate.html'
    model = PonenciaEvento
    form_class = PonenciaEventoForm 
    success_message = "La ponencia en evento '%(titulo)s' ha sido editada con éxito"
    def get_success_url(self):
        return reverse('ponencia_eventos_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PonenciaEventoUpdateView, self).dispatch(*args, **kwargs)
class PonenciaEventoMixin(object):
    model = PonenciaEvento
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'PonenciaEvento'})
        return kwargs
class PonenciaEventoDeleteView(PonenciaEventoMixin, DeleteView):
    template_name = 'FileSampleApp/PonenciaEventodelete_confirm.html'
    def get_success_url(self):
        return reverse('ponencia_eventos_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PonenciaEventoDeleteView, self).dispatch(*args, **kwargs)
class PonenciaEventoDetailView(DetailView):
    template_name = 'FileSampleApp/PonenciaEventoDetails.html'
    model = PonenciaEvento

class ProyectoIDiCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/ProyectoIDiCreateMixin.html'
    model = ProyectoiDi
    form_class = ProyectoIDiForm 
    success_message = "El proyecto IDi '%(titulo)s' ha sido creado con éxito"     
    def get_success_url(self):
        return reverse('proyectoidi_index')    
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(ProyectoIDiCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProyectoIDiCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())
class ProyectoIDiUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/ProyectoIDiUpdate.html'
    model = ProyectoiDi
    form_class = ProyectoIDiForm 
    success_message = "El proyecto IDi '%(titulo)s' ha sido editado con éxito"     
    def get_success_url(self):
        return reverse('proyectoidi_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProyectoIDiUpdateView, self).dispatch(*args, **kwargs)		
class ProyectoIDiMixin(object):
    model = ProyectoiDi
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'ProyectoiDi'})
        return kwargs
class ProyectoIDiDeleteView(ProyectoIDiMixin, DeleteView):
    template_name = 'FileSampleApp/ProyectoIDidelete_confirm.html'
    def get_success_url(self):
        return reverse('proyectoidi_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProyectoIDiDeleteView, self).dispatch(*args, **kwargs)
class ProyectoIDiDetailView(DetailView):
    template_name = 'FileSampleApp/ProyectoIDiDetails.html'
    model = ProyectoiDi


class CapacitacionCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/CapacitacionCreateMixin.html'
    model = Capacitacion
    form_class = CapacitacionForm 
    success_message = "La capacitacion '%(nombre)s' ha sido creada con éxito"   
    def get_success_url(self):
        return reverse('capacitacion_index')                 
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(CapacitacionCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs       
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacitacionCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class CapacitacionUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/CapacitacionUpdate.html'
    model = Capacitacion
    form_class = CapacitacionForm 
    success_message = "La capacitacion '%(nombre)s' ha sido editada con éxito"
    def get_success_url(self):
        return reverse('capacitacion_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacitacionUpdateView, self).dispatch(*args, **kwargs)
class CapacitacionMixin(object):
    model = Capacitacion
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Capacitacion'})
        return kwargs
class CapacitacionDeleteView(CapacitacionMixin, DeleteView):
    template_name = 'FileSampleApp/Capacitaciondelete_confirm.html'
    def get_success_url(self):
        return reverse('capacitacion_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacitacionDeleteView, self).dispatch(*args, **kwargs)
class CapacitacionDetailView(DetailView):
    template_name = 'FileSampleApp/CapacitacionDetails.html'
    model = Capacitacion


class PatenteCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/PatenteCreateMixin.html'
    model = Patente
    form_class = PatenteForm 
    success_message = "La patente '%(nombre_obra)s' ha sido creada con éxito"  
    def get_success_url(self):
        return reverse('patente_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PatenteCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PatenteCreate, self).dispatch(*args, **kwargs)     
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class PatenteUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/PatenteUpdate.html'
    model = Patente
    form_class = PatenteForm 
    success_message = "La patente '%(nombre_obra)s' ha sido editada con éxito"  
    def get_success_url(self):
        return reverse('patente_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PatenteUpdateView, self).dispatch(*args, **kwargs)
class PatenteMixin(object):
    model = Patente
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Patente'})
        return kwargs
class PatenteDeleteView(PatenteMixin, DeleteView):
    template_name = 'FileSampleApp/Patentedelete_confirm.html'
    def get_success_url(self):
        return reverse('patente_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PatenteDeleteView, self).dispatch(*args, **kwargs)
class PatenteDetailView(DetailView):
    template_name = 'FileSampleApp/PatenteDetails.html'
    model = Patente


class ResultadoIntroducidoCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/ResultadoIntroducidoCreateMixin.html'
    model = ResultadoIntroducido
    form_class = ResultadoIntroducidoForm 
    success_message = "El resultado introducido '%(nombre_obra)s' ha sido creado con éxito"
    def get_success_url(self):
        return reverse('resultadointroducido_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(ResultadoIntroducidoCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs  
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultadoIntroducidoCreate, self).dispatch(*args, **kwargs)       
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

class ResultadoIntroducidoUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/ResultadoIntroducidoUpdate.html'
    model = ResultadoIntroducido
    form_class = ResultadoIntroducidoForm 
    success_message = "El resultado introducido '%(nombre_obra)s' ha sido editado con éxito"
    def get_success_url(self):
        return reverse('resultadointroducido_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultadoIntroducidoUpdateView, self).dispatch(*args, **kwargs)
class ResultadoIntroducidoMixin(object):
    model = ResultadoIntroducido
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'ResultadoIntroducido'})
        return kwargs
class ResultadoIntroducidoDeleteView(ResultadoIntroducidoMixin, DeleteView):
    template_name = 'FileSampleApp/ResultadoIntroducidodelete_confirm.html'
    def get_success_url(self):
        return reverse('resultadointroducido_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ResultadoIntroducidoDeleteView, self).dispatch(*args, **kwargs)
class ResultadoIntroducidoDetailView(DetailView):
    template_name = 'FileSampleApp/ResultadoIntroducidoDetails.html'
    model = ResultadoIntroducido		

class PremioCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/PremioCreateMixin.html'
    model = Premio
    form_class = PremioForm 
    success_message = "El premio '%(titulo)s' ha sido creado con éxito"
    def get_success_url(self):
        return reverse('premio_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PremioCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioCreate, self).dispatch(*args, **kwargs) 
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())
		
class PremioPublicacionCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/PremioPublicacionCreateMixin.html'
    model = Premio
    form_class = PremioPublicacionForm 
    success_message = "El premio '%(titulo)s' ha sido creado con éxito"
    def get_success_url(self):
        return reverse('premio_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PremioPublicacionCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioPublicacionCreate, self).dispatch(*args, **kwargs) 
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())		
		
class PremioPonenciaCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/PremioPonenciaCreateMixin.html'
    model = Premio
    form_class = PremioPonenciaForm 
    success_message = "El premio '%(titulo)s' ha sido creado con éxito"
    def get_success_url(self):
        return reverse('premio_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PremioPonenciaCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioPonenciaCreate, self).dispatch(*args, **kwargs) 
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())				
		
class PremioProyectoCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/PremioProyectoCreateMixin.html'
    model = Premio
    form_class = PremioProyectoForm 
    success_message = "El premio '%(titulo)s' ha sido creado con éxito"
    def get_success_url(self):
        return reverse('premio_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PremioProyectoCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioProyectoCreate, self).dispatch(*args, **kwargs) 
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())						

class PremioObraCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/PremioObraCreateMixin.html'
    model = Premio
    form_class = PremioObraForm 
    success_message = "El premio '%(titulo)s' ha sido creado con éxito"
    def get_success_url(self):
        return reverse('premio_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(PremioObraCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioObraCreate, self).dispatch(*args, **kwargs) 
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())								
		
class PremioUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/PremioUpdate.html'
    model = Premio
    form_class = PremioForm 
    success_message = "El premio '%(titulo)s' ha sido editado con éxito"
    def get_success_url(self):
        return reverse('premio_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioUpdateView, self).dispatch(*args, **kwargs)
class PremioMixin(object):
    model = Premio
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Premio'})
        return kwargs
class PremioDeleteView(PremioMixin, DeleteView):
    template_name = 'FileSampleApp/Premiodelete_confirm.html'
    def get_success_url(self):
        return reverse('premio_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PremioDeleteView, self).dispatch(*args, **kwargs)
class PremioDetailView(DetailView):
    template_name = 'FileSampleApp/PremioDetails.html'
    model = Premio		


class EmpleoEstudiantesCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/EmpleoEstudiantesCreateMixin.html'
    model = EmpleoEstudiantes
    form_class = EmpleoEstudiantesForm 
    success_message = "El empleo de estudiantes ha sido creado con éxito"
    def get_success_url(self):
        return reverse('empleoestudiantes_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(EmpleoEstudiantesCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        kwargs['request'] = self.request
        # kwargs['propietario'] = self.request.user
        return kwargs 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesCreate, self).dispatch(*args, **kwargs)  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        # obj.cantidad_estudiantes = self.request.cantidad_estudiantes
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class EmpleoEstudiantesPublicacionCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/EmpleoEstudiantesPublicacionCreateMixin.html'
    model = EmpleoEstudiantes
    form_class = EmpleoEstudiantesPublicacionForm 
    success_message = "El empleo de estudiantes ha sido creado con éxito"
    def get_success_url(self):
        return reverse('empleoestudiantes_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(EmpleoEstudiantesPublicacionCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        kwargs['request'] = self.request
        return kwargs 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesPublicacionCreate, self).dispatch(*args, **kwargs)  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())
		
class EmpleoEstudiantesPonenciaCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/EmpleoEstudiantesPonenciaCreateMixin.html'
    model = EmpleoEstudiantes
    form_class = EmpleoEstudiantesPonenciaForm 
    success_message = "El empleo de estudiantes ha sido creado con éxito"
    def get_success_url(self):
        return reverse('empleoestudiantes_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(EmpleoEstudiantesPonenciaCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        kwargs['request'] = self.request
        return kwargs 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesPonenciaCreate, self).dispatch(*args, **kwargs)  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())		

class EmpleoEstudiantesProyectoCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/EmpleoEstudiantesProyectoCreateMixin.html'
    model = EmpleoEstudiantes
    form_class = EmpleoEstudiantesProyectoForm 
    success_message = "El empleo de estudiantes ha sido creado con éxito"
    def get_success_url(self):
        return reverse('empleoestudiantes_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(EmpleoEstudiantesProyectoCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        kwargs['request'] = self.request
        return kwargs 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesProyectoCreate, self).dispatch(*args, **kwargs)  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())		

class EmpleoEstudiantesObraCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/EmpleoEstudiantesObraCreateMixin.html'
    model = EmpleoEstudiantes
    form_class = EmpleoEstudiantesObraForm 
    success_message = "El empleo de estudiantes ha sido creado con éxito"
    def get_success_url(self):
        return reverse('empleoestudiantes_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(EmpleoEstudiantesObraCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        kwargs['request'] = self.request
        return kwargs 
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesObraCreate, self).dispatch(*args, **kwargs)  
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())		
		
class EmpleoEstudiantesUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/EmpleoEstudiantesUpdate.html'
    model = EmpleoEstudiantes
    form_class = EmpleoEstudiantesForm 
    success_message = "El empleo de estudiantes ha sido modificado con éxito"
    def get_success_url(self):
        return reverse('empleoestudiantes_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesUpdateView, self).dispatch(*args, **kwargs)    
class EmpleoEstudiantesMixin(object):
    model = EmpleoEstudiantes
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'empleo'})
        return kwargs
class EmpleoEstudiantesDeleteView(EmpleoEstudiantesMixin, DeleteView):
    template_name = 'FileSampleApp/EmpleoEstudiantesdelete_confirm.html'
    success_message = "El empleo de estudiantes ha sido eliminado con éxito"
    def get_success_url(self):
        return reverse('empleoestudiantes_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleoEstudiantesDeleteView, self).dispatch(*args, **kwargs)
class EmpleoEstudiantesDetailView(DetailView):
    template_name = 'FileSampleApp/EmpleoEstudiantesDetails.html'
    model = EmpleoEstudiantes        

class NoticiaCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/NoticiaCreateMixin.html'
    model = Noticia
    form_class = NoticiaForm 
    success_message = "La noticia '%(titular)s' ha sido creada con éxito"                            
    def get_success_url(self):
        return reverse('noticia_index')
    # Build the keyword arguments required to instantiate the form
    def get_form_kwargs(self):
        kwargs = super(NoticiaCreate, self).get_form_kwargs()
        kwargs['is_add'] = True
        return kwargs      
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoticiaCreate, self).dispatch(*args, **kwargs)   
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.propietario = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

class NoticiaUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'FileSampleApp/NoticiaUpdate.html'
    model = Noticia
    form_class = NoticiaForm 
    success_message = "La noticia '%(titular)s' ha sido editada con éxito" 
    def get_success_url(self):
        return reverse('noticia_index')    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoticiaUpdateView, self).dispatch(*args, **kwargs)
class NoticiaMixin(object):
    model = Noticia
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Noticia'})
        return kwargs
class NoticiaDeleteView(NoticiaMixin, DeleteView):
    template_name = 'FileSampleApp/Noticiadelete_confirm.html'
    def get_success_url(self):
        return reverse('noticia_index')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoticiaDeleteView, self).dispatch(*args, **kwargs)
class NoticiaDetailView(DetailView):
    template_name = 'FileSampleApp/NoticiaDetails.html'
    model = Noticia
class NoticiaTrabajadorDetailView(DetailView):
    template_name = 'FileSampleApp/NoticiaTrabajadorDetails.html'
    model = Noticia
	

class ModeloYoamelCreate(SuccessMessageMixin, CreateView):
    template_name = 'FileSampleApp/ModeloYoamelCreateMixin.html'
    model = ModeloYoamel
    form_class = ModeloYoamelForm 
    success_url = '/'
    success_message = "El modelo del sitio de Yoamel %(data_title)s ha sido creado con éxito"



class ModelsListView(ListView):
    context_object_name = 'models_list'
    template_name = 'FileSampleApp/ModelsList.html'
    model = ModeloYoamel
    paginate_by = 4



import re

from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

@csrf_exempt
def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.POST) and request.POST['q'].strip():
        query_string = request.POST['q']
        
        entry_query = get_query(query_string, ['title', 'body',])
        
        found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')

    return render_to_response('search/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))

import pprint

@csrf_exempt
def samplePrint(request):
    ds = dict((chr(i), range(i, i+5)) for i in range(65,70))
    response = HttpResponse(pprint.pprint(ds), mimetype='application/force-download')
    return response

@csrf_exempt
def samplePDF(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    return response

@csrf_exempt
def samplePDFF(request):
     # If 'print=pdf' in GET params, then render the PDF!
     # if request.GET.get("print", None) == "pdf":
     #     basename = 'output'  # `.pdf` will be appended to this string.
     #     return render_to_pdf(request, basename)
     # else:
     #     return HttpResponse("Hello World!")
        file_name = '/tmp/current_page.pdf'
        url = ('user_current_url')
        external_process = Popen(["phantomjs", phantomjs_script, url, file_name],
                                 stdout=PIPE, stderr=STDOUT)
        # Open the file created by PhantomJS
        return_file = File(open(file_name, 'r'))
        response = HttpResponse(return_file, mimetype='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=current_page.pdf'
        # Return the file to the browser and force it as download item
        return response

@csrf_exempt
def sampleCSV(request):
    response = HttpResponse(content_type='application/xls')
    response['Content-Disposition'] = 'attachment; filename="somefile.xls"'
    response["Content-Transfer-Encoding"] = "binary";
    writer = csv.writer(response)
    allclientes = [(p.nombre) for p in Capacitacion.objects.all()]
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])

    #writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

import io
from django.utils.translation import ugettext
import xlsxwriter, datetime
from django.conf import settings

def capacitacionesCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Capacitaciones.xlsx'
    xlsx_data = WriteToExcel("Capacitacion", request)
    response.write(xlsx_data)
    return response

def WriteToExcel(page, request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    # Here we will adding the code to add data
    worksheet_s = workbook.add_worksheet("Summary")
    title = workbook.add_format({
    'bold': True,
    'font_size': 14,
    'align': 'center',
    'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    cell = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    cell_center = workbook.add_format({
        'align': 'center',
        'valign': 'top',
        'border': 1
    })

    if page == "Capacitacion":
        title_text = u"{0} {1} {2}".format(ugettext("Capacitaciones correspondientes a "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Nombre"), header)
        worksheet_s.write(4, 2, ugettext("Tipo"), header)
        worksheet_s.write(4, 3, ugettext(u"Fecha"), header)
        worksheet_s.write(4, 4, ugettext(u"Rol"), header)
        worksheet_s.write(4, 5, ugettext(u"Modalidad"), header)
        worksheet_s.write(4, 6, ugettext(u"Institución"), header)
        worksheet_s.write(4, 7, ugettext(u"País"), header)
        worksheet_s.write(4, 8, ugettext(u"Ciudad"), header)

        description_col_width = 10    

        capacitaciones = Capacitacion.objects.filter(propietario_id=request.user.id)

        for idx, data in enumerate(capacitaciones):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.nombre, cell)
            worksheet_s.write_string(row, 2, data.tipo.nombre, cell)
            worksheet_s.write(row, 3, data.fecha.strftime('%d/%m/%Y'), cell_center)
            worksheet_s.write_string(row, 4, data.rol.nombre, cell)
            worksheet_s.write_string(row, 5, data.modalidad.nombre, cell)
            worksheet_s.write_string(row, 6, data.institucion, cell)
            worksheet_s.write_string(row, 7, data.pais.nombre, cell)
            worksheet_s.write_string(row, 8, data.ciudad.nombre, cell)
        worksheet_s.set_column('B:B', 55)            
        worksheet_s.set_column('D:D', 15)
        worksheet_s.set_column('F:F', 50)
        worksheet_s.set_column('G:G', 50)
        worksheet_s.set_column('H:H', 50)
        worksheet_s.set_column('I:I', 50)
    elif page == "Publicacion":
        title_text = u"{0} {1} {2}".format(ugettext("Publicaciones correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Titulo"), header)
        # worksheet_s.write(4, 2, ugettext("Autor"), header)
        # worksheet_s.write(4, 2, ugettext(u"Nivel de Autoría"), header)
        worksheet_s.write(4, 2, ugettext(u"Año"), header)
        worksheet_s.write(4, 3, ugettext(u"Pais"), header)
        worksheet_s.write(4, 4, ugettext(u"Ciudad"), header)
        worksheet_s.write(4, 5, ugettext(u"Editorial"), header)
        worksheet_s.write(4, 6, ugettext(u"Publicación"), header)
        worksheet_s.write(4, 7, ugettext(u"Número"), header)
        worksheet_s.write(4, 8, ugettext(u"Volumen"), header)
        worksheet_s.write(4, 9, ugettext(u"Nivel MES"), header)
        worksheet_s.write(4, 10, ugettext(u"Aprobación"), header)

        publicaciones = Publicacion.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(publicaciones):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.titulo, cell)
            # worksheet_s.write_string(row, 2, data.autor, cell)
            # worksheet_s.write_string(row, 2, data.nivel_autoria.nombre, cell_center)
            worksheet_s.write_string(row, 2, data.anno, cell_center)
            worksheet_s.write_string(row, 3, data.pais.nombre, cell)
            worksheet_s.write_string(row, 4, data.ciudad.nombre, cell)
            worksheet_s.write_string(row, 5, data.editorial, cell)
            worksheet_s.write_string(row, 6, data.publicacion, cell)
            worksheet_s.write_number(row, 7, data.numero, cell_center)
            worksheet_s.write_number(row, 8, data.volumen, cell_center)
            worksheet_s.write_string(row, 9, data.nivel_mes.nombre, cell_center)
            worksheet_s.write_boolean(row, 10, data.aprobacion, cell_center)
            
        worksheet_s.set_column('B:B', 55)            
        worksheet_s.set_column('D:D', 15)
        worksheet_s.set_column('F:F', 50)
        worksheet_s.set_column('G:G', 50)
        worksheet_s.set_column('H:H', 50)
        worksheet_s.set_column('I:I', 50)
        worksheet_s.set_column('L:L', 15)
        worksheet_s.set_column('M:M', 15)
    elif page == "Evento":
        title_text = "Listado de Eventos"
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Nombre"), header)
        worksheet_s.write(4, 2, ugettext("Edición"), header)
        worksheet_s.write(4, 3, ugettext(u"Nivel"), header)
        worksheet_s.write(4, 4, ugettext(u"Pais"), header)
        worksheet_s.write(4, 5, ugettext(u"Ciudad"), header)
        worksheet_s.write(4, 6, ugettext(u"Tipo de publicacion"), header)
        worksheet_s.write(4, 7, ugettext(u"ISSN"), header)

        eventos = Evento.objects.all()
        for idx, data in enumerate(eventos):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.nombre, cell)
            worksheet_s.write_number(row, 2, data.edicion, cell_center)
            worksheet_s.write_string(row, 3, data.nivel.nombre, cell)
            worksheet_s.write_string(row, 4, data.pais.nombre, cell)
            worksheet_s.write_string(row, 5, data.ciudad.nombre, cell)
            worksheet_s.write_string(row, 6, data.tipo_publicacion.nombre, cell)
            worksheet_s.write_string(row, 7, data.issn, cell_center)
            
        worksheet_s.set_column('B:B', 55)            
        worksheet_s.set_column('D:D', 15)
        worksheet_s.set_column('E:E', 50)
        worksheet_s.set_column('F:F', 50)
        worksheet_s.set_column('G:G', 50)
        worksheet_s.set_column('H:H', 50)
        worksheet_s.set_column('I:I', 50)
    elif page == "Ponencia":
        title_text = u"{0} {1} {2}".format(ugettext("Ponencias correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Titulo"), header)
        worksheet_s.write(4, 2, ugettext("Evento"), header)
        # worksheet_s.write(4, 3, ugettext(u"Autor"), header)
        # worksheet_s.write(4, 4, ugettext(u"Nivel de Autoría"), header)

        ponencias = PonenciaEvento.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(ponencias):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.titulo, cell)
            worksheet_s.write_string(row, 2, data.evento.nombre, cell)
            # worksheet_s.write_string(row, 3, data.autor, cell)
            # worksheet_s.write_string(row, 4, data.nivel_autoria.nombre, cell_center)

        worksheet_s.set_column('B:B', 75)
        worksheet_s.set_column('C:C', 75)                        
        # worksheet_s.set_column('D:D', 15)
        # worksheet_s.set_column('E:E', 15)
    elif page == "Patente":
        title_text = u"{0} {1} {2}".format(ugettext("Patentes correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Nombre de Obra"), header)
        worksheet_s.write(4, 2, ugettext("Ciencia de Obra"), header)
        worksheet_s.write(4, 3, ugettext(u"Fecha"), header)
        worksheet_s.write(4, 4, ugettext(u"Tipo de Obra"), header)
        worksheet_s.write(4, 5, ugettext(u"Fuente de Registro"), header)
        worksheet_s.write(4, 6, ugettext(u"Cantidad de autores"), header)
        worksheet_s.write(4, 7, ugettext(u"Comentario"), header)

        patentes = Patente.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(patentes):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.nombre_obra.titulo, cell)
            worksheet_s.write_string(row, 2, data.ciencia_obra.nombre, cell)
            worksheet_s.write(row, 3, data.fecha.strftime('%d/%m/%Y'), cell_center)
            worksheet_s.write_string(row, 4, data.tipo_obra.nombre, cell)
            worksheet_s.write_string(row, 5, data.fuente_registro, cell)
            worksheet_s.write_number(row, 6, data.cantidad_autores, cell_center)
            worksheet_s.write_string(row, 7, data.comentario, cell)

        worksheet_s.set_column('B:B', 75)            
        worksheet_s.set_column('C:C', 15)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 20)
        worksheet_s.set_column('F:F', 20)
        worksheet_s.set_column('G:G', 20)
        worksheet_s.set_column('H:H', 20)
    elif page == "Resultado":
        title_text = u"{0} {1} {2}".format(ugettext("Resultados introducidos correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Nombre de Obra"), header)
        worksheet_s.write(4, 2, ugettext("Ciencia de Obra"), header)
        worksheet_s.write(4, 3, ugettext(u"Fecha"), header)
        worksheet_s.write(4, 4, ugettext(u"Tipo de Obra"), header)
        worksheet_s.write(4, 5, ugettext(u"Tamaño"), header)
        worksheet_s.write(4, 6, ugettext(u"Institución"), header)
        worksheet_s.write(4, 7, ugettext(u"Cantidad de autores"), header)
        worksheet_s.write(4, 8, ugettext(u"Comentario"), header)

        resultados = ResultadoIntroducido.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(resultados):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.nombre_obra.titulo, cell)
            worksheet_s.write_string(row, 2, data.ciencia_obra.nombre, cell)
            worksheet_s.write(row, 3, data.fecha.strftime('%d/%m/%Y'), cell_center)
            worksheet_s.write_string(row, 4, data.tipo_obra.nombre, cell)
            worksheet_s.write_string(row, 5, data.tamanno.nombre, cell)
            worksheet_s.write_string(row, 6, data.institucion, cell)
            worksheet_s.write_number(row, 7, data.cantidad_autores, cell_center)
            worksheet_s.write_string(row, 8, data.comentario, cell)

        worksheet_s.set_column('B:B', 75)            
        worksheet_s.set_column('C:C', 15)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 20)
        worksheet_s.set_column('F:F', 20)
        worksheet_s.set_column('G:G', 20)
        worksheet_s.set_column('H:H', 20)
        worksheet_s.set_column('I:I', 140)
    elif page == "Premio":
        title_text = u"{0} {1} {2}".format(ugettext("Premios correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Titular"), header)
        # worksheet_s.write(4, 2, ugettext("Autor"), header)
        # worksheet_s.write(4, 3, ugettext(u"Nivel de Autoria"), header)
        worksheet_s.write(4, 2, ugettext(u"Año"), header)
        worksheet_s.write(4, 3, ugettext(u"País"), header)
        worksheet_s.write(4, 4, ugettext(u"Ciudad"), header)
        worksheet_s.write(4, 5, ugettext(u"Lugar del premio"), header)
        worksheet_s.write(4, 6, ugettext(u"Nivel"), header)
        worksheet_s.write(4, 7, ugettext(u"Caracter"), header)

        premios = Premio.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(premios):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.titulo, cell)
            # worksheet_s.write_string(row, 2, data.autor, cell)
            # worksheet_s.write_string(row, 3, data.nivel_autoria.nombre, cell_center)
            worksheet_s.write_number(row, 2, data.anno, cell_center)
            worksheet_s.write_string(row, 3, data.pais.nombre, cell)
            worksheet_s.write_string(row, 4, data.ciudad.nombre, cell_center)
            worksheet_s.write_string(row, 5, data.lugar_premio.nombre, cell_center)
            worksheet_s.write_string(row, 6, data.nivel_premio.nombre, cell_center)
            worksheet_s.write_string(row, 7, data.caracter.nombre, cell_center)

        worksheet_s.set_column('B:B', 75)            
        worksheet_s.set_column('C:C', 15)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 20)
        worksheet_s.set_column('F:F', 20)
        worksheet_s.set_column('G:G', 20)
        worksheet_s.set_column('H:H', 20)
        worksheet_s.set_column('I:I', 20)
    elif page == "Noticia":
        title_text = u"{0} {1} {2}".format(ugettext("Noticias correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Titular"), header)
        worksheet_s.write(4, 2, ugettext("Rango de Tiempo"), header)
        worksheet_s.write(4, 3, ugettext(u"Publicación"), header)
        worksheet_s.write(4, 4, ugettext(u"Tiempo de visibilidad"), header)
        worksheet_s.write(4, 5, ugettext(u"Caracter"), header)
        worksheet_s.write(4, 6, ugettext(u"Contenido"), header)
        worksheet_s.write(4, 7, ugettext(u"Aprobación"), header)

        noticias = Noticia.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(noticias):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.titular, cell)
            worksheet_s.write_string(row, 2, data.rango_tiempo, cell)
            worksheet_s.write(row, 3, data.publicacion.strftime('%d/%m/%Y'), cell_center)
            worksheet_s.write_string(row, 4, data.tiempo_visibilidad, cell_center)
            worksheet_s.write_string(row, 5, data.caracter.nombre, cell)
            worksheet_s.write_string(row, 6, data.contenido, cell_center)
            worksheet_s.write_boolean(row, 7, data.aprobacion, cell_center)

        worksheet_s.set_column('B:B', 75)            
        worksheet_s.set_column('C:C', 15)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 20)
        worksheet_s.set_column('F:F', 20)
        worksheet_s.set_column('G:G', 20)
        worksheet_s.set_column('H:H', 20)
        worksheet_s.set_column('I:I', 20)
    elif page == "EmpleoEstudiantes":
        title_text = u"{0} {1} {2}".format(ugettext("Empleo de Estudiantes correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Fuente"), header)
        worksheet_s.write(4, 2, ugettext("Nombre de Fuente"), header)
        worksheet_s.write(4, 3, ugettext(u"Nombre de Obra"), header)
        worksheet_s.write(4, 4, ugettext(u"Cantidad de estudiantes"), header)

        empleoestudiantes = EmpleoEstudiantes.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(empleoestudiantes):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.fuente.nombre, cell)
            worksheet_s.write_string(row, 2, data.nombre_fuente, cell)
            worksheet_s.write_string(row, 3, data.nombre_obra.titulo, cell)
            worksheet_s.write_string(row, 4, data.cantidad_estudiantes, cell_center)

        worksheet_s.set_column('B:B', 55)            
        worksheet_s.set_column('C:C', 60)
        worksheet_s.set_column('D:D', 140)
        worksheet_s.set_column('E:E', 30)

    elif page == "ObraCientifica":
        title_text = u"{0} {1} {2}".format(ugettext("Obras científicas correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Titulo"), header)
        worksheet_s.write(4, 2, ugettext("Tipo de obra"), header)
        worksheet_s.write(4, 3, ugettext(u"Fecha de creacion"), header)
        worksheet_s.write(4, 4, ugettext(u"Tamaño"), header)
        worksheet_s.write(4, 5, ugettext(u"Descripción"), header)

        obraCientifica = ObraCientifica.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(obraCientifica):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.titulo, cell)
            worksheet_s.write_string(row, 2, data.tipo_obra.nombre, cell)
            worksheet_s.write_string(row, 3, data.fecha_creacion.strftime('%d/%m/%Y'), cell_center)
            worksheet_s.write_string(row, 4, data.tamanno.nombre, cell_center)
            worksheet_s.write_string(row, 5, data.descripcion, cell)

        worksheet_s.set_column('B:B', 55)            
        worksheet_s.set_column('C:C', 20)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 15)
        worksheet_s.set_column('F:F', 70)

    elif page == "ProyectoIDi":
        title_text = u"{0} {1} {2}".format(ugettext("Proyectos IDi correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Titulo"), header)
        worksheet_s.write(4, 2, ugettext("Nivel"), header)
        worksheet_s.write(4, 3, ugettext(u"Area Ejecutora"), header)
        worksheet_s.write(4, 4, ugettext(u"Linea Cientifica"), header)

        proyectos = ProyectoiDi.objects.filter(propietario_id=request.user.id)
        for idx, data in enumerate(proyectos):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.titulo, cell)
            worksheet_s.write_string(row, 2, data.nivel.nombre, cell)
            worksheet_s.write_string(row, 3, data.area_ejecutora.nombre, cell_center)
            worksheet_s.write_string(row, 4, data.linea_cientifica.nombre, cell)

        worksheet_s.set_column('B:B', 55)            
        worksheet_s.set_column('C:C', 30)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 70)

    elif page == "SAI":
        title_text = u"{0} {1} {2}".format(ugettext("SAI correspondientes a: "), request.user.first_name, request.user.last_name)
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Area solicitante"), header)
        worksheet_s.write(4, 2, ugettext("Fecha"), header)
        worksheet_s.write(4, 3, ugettext(u"Codigo"), header)
        worksheet_s.write(4, 4, ugettext(u"Tipo SAI"), header)
        worksheet_s.write(4, 5, ugettext(u"SubTipo SAI"), header)
        worksheet_s.write(4, 6, ugettext(u"Cantidad de personas a recibir el servicio solicitado"), header)
        worksheet_s.write(4, 7, ugettext(u"Tematica del servicio solicitado"), header)

        sais = SAI.objects.filter(solicitante_id=request.user.id)
        for idx, data in enumerate(sais):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.area_solicitante, cell)
            worksheet_s.write_string(row, 2, data.fecha.strftime('%d/%m/%Y'), cell)
            worksheet_s.write_string(row, 3, data.codigo, cell_center)
            worksheet_s.write_string(row, 4, data.tipo_SAI.nombre, cell)
            worksheet_s.write_string(row, 5, data.subtipo_SAI.nombre, cell)
            worksheet_s.write_string(row, 6, data.personal_SAI.nombre, cell)
            worksheet_s.write_string(row, 7, data.tematica_SAI.nombre, cell)

        worksheet_s.set_column('B:B', 55)            
        worksheet_s.set_column('C:C', 30)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 70)        
        worksheet_s.set_column('F:F', 70)        
        worksheet_s.set_column('G:G', 70)        
        worksheet_s.set_column('H:H', 70)      

    elif page == "User":
        title_text = "Listado de usuarios registrados en SAISA"
        worksheet_s.merge_range('B2:H2', title_text, title)
        worksheet_s.write(4, 0, ugettext("#"), cell_center)
        worksheet_s.write(4, 1, ugettext("Nombre"), header)
        worksheet_s.write(4, 2, ugettext("Apellidos"), header)
        worksheet_s.write(4, 3, ugettext(u"Usuario"), header)
        worksheet_s.write(4, 4, ugettext(u"Correo electrónico"), header)

        users = User.objects.all()
        for idx, data in enumerate(users):
            row = 5 + idx
            worksheet_s.write_number(row, 0, idx + 1, cell_center)
            worksheet_s.write_string(row, 1, data.first_name, cell)
            worksheet_s.write_string(row, 2, data.last_name, cell)
            worksheet_s.write_string(row, 3, data.username, cell_center)
            worksheet_s.write_string(row, 4, data.email, cell)

        worksheet_s.set_column('B:B', 40)            
        worksheet_s.set_column('C:C', 40)
        worksheet_s.set_column('D:D', 20)
        worksheet_s.set_column('E:E', 70)        
        worksheet_s.set_column('F:F', 70)        
    # the rest of the headers from the HTML file

    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data

class InvestigadorDetailView(DetailView):
    template_name = 'FileSampleApp/InvestigadorDetails.html'
    model = User

def publicacionesCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Publicaciones.xlsx'
    xlsx_data = WriteToExcel("Publicacion", request)
    response.write(xlsx_data)
    return response  

def eventosCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Eventos.xlsx'
    xlsx_data = WriteToExcel("Evento", request)
    response.write(xlsx_data)
    return response     

def ponenciasCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Ponencias.xlsx'
    xlsx_data = WriteToExcel("Ponencia", request)
    response.write(xlsx_data)
    return response

def patentesCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Patentes.xlsx'
    xlsx_data = WriteToExcel("Patente", request)
    response.write(xlsx_data)
    return response        

def resultadosCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Resultados Introducidos.xlsx'
    xlsx_data = WriteToExcel("Resultado", request)
    response.write(xlsx_data)
    return response

def premiosCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Premios.xlsx'
    xlsx_data = WriteToExcel("Premio", request)
    response.write(xlsx_data)
    return response

def noticiasCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Noticias.xlsx'
    xlsx_data = WriteToExcel("Noticia", request)
    response.write(xlsx_data)
    return response

def empleoEstudiantesCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Empleo de Estudiantes.xlsx'
    xlsx_data = WriteToExcel("EmpleoEstudiantes", request)
    response.write(xlsx_data)
    return response

def ObraCientificaCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Obras Cientificas.xlsx'
    xlsx_data = WriteToExcel("ObraCientifica", request)
    response.write(xlsx_data)
    return response

def ProyectoIDiCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Proyectos IDi.xlsx'
    xlsx_data = WriteToExcel("ProyectoIDi", request)
    response.write(xlsx_data)
    return response

def SAICSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Servicios Academico-Investigativos.xlsx'
    xlsx_data = WriteToExcel("SAI", request)
    response.write(xlsx_data)
    return response
	
def UsuariosCSV(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado de Usuarios.xlsx'
    xlsx_data = WriteToExcel("User", request)
    response.write(xlsx_data)
    return response	

def Ranking(request):
    return render(request, 'FileSampleApp/Ranking.html')                          

def Resultados(request):
    return render(request, 'FileSampleApp/Resultados.html')     

def InformeCienciaTecnica(request):
    return render(request, 'FileSampleApp/InformeCienciaTecnica.html')  

from wkhtmltopdf.views import PDFTemplateResponse, PDFTemplateView
from django.views.generic.base import View

def MyPDFViewPublicaciones(request):
    objectContext = Publicacion.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/PublicacionesPdf.html",
                               {"user":request.user,"object":objectContext})
    # template='FileSampleApp/PublicacionesPdf.html'
    # context= {'publicaciones': Publicacion.objects.all()}
    # def get(self, request):
    #     response = PDFTemplateResponse(request=request,
    #                                    template=self.template,
    #                                    filename="ListadoPublicaciones.pdf",
    #                                    context= self.context,
    #                                    show_content_in_browser=True,
    #                                    cmd_options={'margin-top': 10,},
    #                                    )
    #     return response  

class MyPDFViewEventos(View):
    template='FileSampleApp/EventosPdf.html'
    context= {'eventos': Evento.objects.all()}
    def get(self, request):
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="ListadoEventos.pdf",
                                       context= self.context,
                                       show_content_in_browser=True,
                                       cmd_options={'margin-top': 10,},
                                       )
        return response  

def MyPDFViewPonencias(request):
    objectContext = PonenciaEvento.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/PonenciasPdf.html",
                               {"user":request.user,"object":objectContext})
    # template='FileSampleApp/PonenciasPdf.html'
    # context= {'ponencias': PonenciaEvento.objects.all()}
    # def get(self, request):
    #     response = PDFTemplateResponse(request=request,
    #                                    template=self.template,
    #                                    filename="ListadoPonencias.pdf",
    #                                    context= self.context,
    #                                    show_content_in_browser=True,
    #                                    cmd_options={'margin-top': 10,},
    #                                    )
    #     return response       

def MyPDFViewCapacitaciones(request):
    objectContext = Capacitacion.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/CapacitacionesPdf.html",
                               {"user":request.user,"object":objectContext})
    # template='FileSampleApp/CapacitacionesPdf.html'
    # context= {'capacitaciones': Capacitacion.objects.all()}
    # def get(self, request):
    #     response = PDFTemplateResponse(request=request,
    #                                    template=self.template,
    #                                    filename="ListadoCapacitaciones.pdf",
    #                                    context= self.context,
    #                                    show_content_in_browser=True,
    #                                    cmd_options={'margin-top': 10,},
    #                                    )
    #     return response     

def MyPDFViewPatentes(request):
    objectContext = Patente.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/PatentesPdf.html",
                               {"user":request.user,"object":objectContext})
    # template='FileSampleApp/PatentesPdf.html'
    # context= {'patentes': Patente.objects.all()}
    # def get(self, request):
    #     response = PDFTemplateResponse(request=request,
    #                                    template=self.template,
    #                                    filename="ListadoPatentes.pdf",
    #                                    context= self.context,
    #                                    show_content_in_browser=True,
    #                                    cmd_options={'margin-top': 10,},
    #                                    )
    #     return response   

def MyPDFViewResultadosIntroducidos(request):
    objectContext = ResultadoIntroducido.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/ResultadosIntroducidosPdf.html",
                               {"user":request.user,"object":objectContext})
    # template='FileSampleApp/ResultadosIntroducidosPdf.html'
    # context= {'resultados': ResultadoIntroducido.objects.all()}
    # def get(self, request):
    #     response = PDFTemplateResponse(request=request,
    #                                    template=self.template,
    #                                    filename="ListadoResultadosIntroducidos.pdf",
    #                                    context= self.context,
    #                                    show_content_in_browser=True,
    #                                    cmd_options={'margin-top': 10,},
    #                                    )
    #     return response           

def MyPDFViewPremios(request):
    objectContext = Premio.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/PremiosPdf.html",
                               {"user":request.user,"object":objectContext})
    # template='FileSampleApp/PremiosPdf.html'
    # context= {'premios': Premio.objects.all()}
    # def get(self, request):
    #     response = PDFTemplateResponse(request=request,
    #                                    template=self.template,
    #                                    filename="ListadoPremios.pdf",
    #                                    context= self.context,
    #                                    show_content_in_browser=True,
    #                                    cmd_options={'margin-top': 10,},
    #                                    )
    #     return response    

def MyPDFViewEmpleoEstudiantes(request):
    objectContext = EmpleoEstudiantes.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/EmpleoEstudiantesPdf.html",
                               {"user":request.user,"object":objectContext})
    # template='FileSampleApp/EmpleoEstudiantesPdf.html'
    # context= {'empleoestudiantes': EmpleoEstudiantes.objects.all()}
    # def get(self, request):
    #     response = PDFTemplateResponse(request=request,
    #                                    template=self.template,
    #                                    filename="ListadoEmpleoEstudiantes.pdf",
    #                                    context= self.context,
    #                                    show_content_in_browser=True,
    #                                    cmd_options={'margin-top': 10,},

    #                                    )
    #     return response    

def MyPDFViewNoticias(request):
    objectContext = Noticia.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/NoticiasPdf.html",
                               {"user":request.user,"object":objectContext})
def MyPDFViewObrasCientificas(request):
    objectContext = ObraCientifica.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/ObrasCientificasPdf.html",
                               {"user":request.user,"object":objectContext})
def MyPDFViewProyectosIDi(request):
    objectContext = ProyectoiDi.objects.filter(propietario_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/ProyectosIDiPdf.html",
                               {"user":request.user,"object":objectContext})

def MyPDFViewSAI(request):
    objectContext = SAI.objects.filter(solicitante_id=request.user.id)
    return PDFTemplateResponse(request,
                               "FileSampleApp/SAIPdf.html",
                               {"user":request.user,"object":objectContext})
							   
def MyPDFViewUsers(request):
    objectContext = User.objects.all()
    return PDFTemplateResponse(request,
                               "FileSampleApp/UsuariosPdf.html",
                               {"user":request.user,"object":objectContext})							   