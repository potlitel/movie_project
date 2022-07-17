from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from FileSample.models import (Ciudad, Publicacion, Evento, PonenciaEvento,
    Capacitacion, Patente, ResultadoIntroducido, Premio, EmpleoEstudiantes, Noticia, User,
    Profile, ObraCientifica, Publicacion, PonenciaEvento, ProyectoiDi)
# from django.utils import smart_unicode
# from django.utils import simplejson

@csrf_exempt
def test(request):
    response = []

    
@csrf_exempt
def get_sectors(request):
    response = []
    industry_id = int(request.POST['id_pais'])

    # With the sector_id you know wich sector the user has selected
    # You should generate the list based in your needs
    data = []
    if industry_id:
        # sectors = INDUSTRY_DICT[industry_id]  # This return a list of ID's of sectors
        # Then make loop over all sectors
        for sector_id in sectors:  
            # To get the sector name you should use another dict
            # I think you already have it in USER_PROFILE_CURRENT_SECTOR_TYPES
            # Remember to import it (check above)
            # sector_name =  USER_PROFILE_CURRENT_SECTOR_TYPES[sector_id]
            # We append the id and the name to replace options in the HTML
            # data.append({'id':sector_id, 'name':sector_name})  

            data.append({'id':1, 'name':'get_ciudades'})  

        response = { 'item_list':data }  # We send back the list
        return HttpResponse(simplejson.dumps(response))

    # If we get any error, or cannot get the sector, we send an empty response
    response = {}
    return HttpResponse(simplejson.dumps(response))

class JSONResponse(HttpResponse):
    def __init__(self, data):
        super(JSONResponse, self).__init__(
                simplejson.dumps(data), mimetype='application/json')

@csrf_exempt
def municipalities_for_county(request):
    if request.is_ajax() and request.GET and 'county_id' in request.GET:
        objs = Municipality.objects.filter(county=request.GET['county_id'])
        return JSONResponse([{'id': o.id, 'name': smart_unicode(o)}
            for o in objs])
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})    



@csrf_exempt
def delete_post(request):
    if request.method == 'POST':

        # post = Ciudad.objects.get(pk=int(QueryDict(request.body).get('postpk')))

        # post.delete()

        response_data = {}
        response_data['msg'] = 'Post was deleted.'

        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type="application/json"
        # )
        # obj = Ciudad.objects.all()
        obj = Ciudad.objects.filter(pais=request.POST['postpk'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        # return HttpResponse(
        #     json.dumps({"nothing to see": "this isn't happening"}),
        #     content_type="application/json"
        # )
        return JSONResponse({'error': 'Not Ajax or no GET'})    


@csrf_exempt
def searchPublicacion(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Publicacion.objects.filter(titulo=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})

@csrf_exempt
def searchEvento(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Evento.objects.filter(nombre=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})

@csrf_exempt
def searchPonenciaEvento(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = PonenciaEvento.objects.filter(titulo=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})  

@csrf_exempt
def searchCapacitacion(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Capacitacion.objects.filter(nombre=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})                

@csrf_exempt
def searchPatente(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Patente.objects.filter(nombre_obra=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})                        

@csrf_exempt
def searchResultadoIntroducido(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = ResultadoIntroducido.objects.filter(nombre_obra=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})                                

@csrf_exempt
def searchPremio(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Premio.objects.filter(titulo=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})                                        

@csrf_exempt
def searchNoticia(request):
    if request.method == 'POST':
        response_data = {}
        response_data['msg'] = 'Post was deleted.'
        obj = Noticia.objects.filter(titular=request.POST['criterio'])
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JSONResponse({'error': 'Not Ajax or no GET'})                                        

from preserialize.serialize import serialize
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
@csrf_exempt
def getInvestigadores(request):
    response = []
    if request.method == 'POST':
        #obj = User.objects.all().select_related('profile')
        #obj = User.objects.filter(perfil__cargo=10).prefetch_related('perfil')
        #obj = User.objects.filter(perfil__cargo=10)
        if request.POST['id'] == "todos":
            obj = User.objects.filter(Q(perfil__cargo=1) | Q(perfil__cargo=2) | Q(perfil__cargo=5) | Q(perfil__cargo=6) | Q(perfil__cargo=7) | Q(perfil__cargo=11)).prefetch_related('perfil')
        else:
            if request.POST['id'] == "centroEstudios":
               obj = ""
            else:
               if request.POST['id'] == "colaborador":
                  obj = User.objects.filter(perfil__cargo=11).prefetch_related('perfil')
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({"Nothing to see": "this isn't happening"})        
		
		
@csrf_exempt
def getObrasCientificas(request):
    response = []
    if request.method == 'POST':
        obj = ObraCientifica.objects.all()
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({"Nothing to see": "this isn't happening"})        		
		
@csrf_exempt
def getPublicaciones(request):
    response = []
    if request.method == 'POST':
        obj = Publicacion.objects.all()
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({"Nothing to see": "this isn't happening"})        		

@csrf_exempt
def getPonencias(request):
    response = []
    if request.method == 'POST':
        obj = PonenciaEvento.objects.all()
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({"Nothing to see": "this isn't happening"})        		

@csrf_exempt
def getProyectos(request):
    response = []
    if request.method == 'POST':
        obj = ProyectoiDi.objects.all()
        data = serializers.serialize('json', obj)
        return HttpResponse(data,'json')
    else:
        return JsonResponse({"Nothing to see": "this isn't happening"})        				