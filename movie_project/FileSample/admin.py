from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# Register your models here.
from FileSample.models import (Continent, Country, Pais, Ciudad, Publicacion, 
	ProyectoiDi, Membresia, TipoObraCientifica, NivelAutoria, NivelMES, NivelEvento
	, TipoPublicacion, TipoCapacitacion, RolCapacitación, ModalidadCapacitacion,
	CienciaObra, TipoObra, TamañoObra, LugarPremio, CaracterPremio, Fuente, CaracterNoticia, 
	Area, Grupo, NivelProyecto, LineaCientificaProyecto, TipoSAISolicitado, SubTipoSAISolicitado,
	TematicaSAI, PersonalRecibirSAI, TiempoSAI, EvaluacionSAI, SAI, Provincia, Municipio,
	Cargo, CategoriaDocente, GradoCientifico, Sexo, TituloAcademico, Rol, Profile)
from django.contrib.auth.models import User

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(TipoObraCientifica)
admin.site.register(NivelAutoria)
admin.site.register(NivelMES)
admin.site.register(NivelEvento)
admin.site.register(TipoPublicacion)
admin.site.register(TipoCapacitacion)
admin.site.register(RolCapacitación)
admin.site.register(ModalidadCapacitacion)
admin.site.register(CienciaObra)
admin.site.register(TipoObra)
admin.site.register(TamañoObra)
admin.site.register(LugarPremio)
admin.site.register(CaracterPremio)
admin.site.register(Fuente)
admin.site.register(CaracterNoticia)
admin.site.register(Area)
admin.site.register(Grupo)
admin.site.register(NivelProyecto)
admin.site.register(LineaCientificaProyecto)
admin.site.register(TipoSAISolicitado)
admin.site.register(SubTipoSAISolicitado)
admin.site.register(TematicaSAI)
admin.site.register(PersonalRecibirSAI)
admin.site.register(TiempoSAI)
admin.site.register(EvaluacionSAI)
admin.site.register(SAI)
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Cargo)
admin.site.register(CategoriaDocente)
admin.site.register(GradoCientifico)
admin.site.register(Sexo)
admin.site.register(TituloAcademico)
admin.site.register(Rol)
admin.site.register(ProyectoiDi)

# class MembershipInline(admin.TabularInline):
    # model = Membresia
    # extra = 1

# class ProyectoIDIAdmin(admin.ModelAdmin):
    # inlines = (MembershipInline,)

# class PublicacionAdmin(admin.ModelAdmin):
    # inlines = (MembershipInline,)    

#admin.site.register(ProyectoiDi, ProyectoIDIAdmin)
# admin.site.register(Publicacion, PublicacionAdmin)

class UserProfileInline(admin.TabularInline):
    model = Profile

class UserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)