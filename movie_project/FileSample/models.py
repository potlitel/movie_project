from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from any_imagefield.models import AnyImageField
from django.forms.extras.widgets import SelectDateWidget
from smart_selects.db_fields import ChainedForeignKey
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from FileSample.validators import propietario
from sortedm2m.fields import SortedManyToManyField
from django.db.models import ManyToManyField
from django.contrib.auth.models import User
from django.conf import settings

alphanumeric = RegexValidator(r'^[0-9a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')
alpha = RegexValidator(r'^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')
numeric = RegexValidator(r'^[0-9]*$', 'Has introducido caracteres incorrectos.')
comment = RegexValidator(r'^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')

# Create your models here.
GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female')
)

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad PROFILE
"""""""""""""""""""""""""""""""""""""""""""""""""""
class Provincia(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Provincias'
        verbose_name = 'Provincia'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class Municipio(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      provincia = models.ForeignKey(Provincia)
      class Meta:
        verbose_name_plural = 'Municipios'
        verbose_name = 'Municipio'
        ordering = ['nombre']
      def __str__(self):
        return self.nombre   

class Cargo(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Cargos'
        verbose_name = 'Cargo'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre     

class CategoriaDocente(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Categorias Docentes'
        verbose_name = 'Categoria Docente'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre  

class GradoCientifico(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Grados Cientificos'
        verbose_name = 'Grado Cientifico'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre      
        
class Sexo(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Sexos'
        verbose_name = 'Sexo'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre  

class TituloAcademico(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Titulos Academicos'
        verbose_name = 'Titulo Academico'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre                              

class Rol(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Roles'
        verbose_name = 'Rol'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre            

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad PUBLICACION
"""""""""""""""""""""""""""""""""""""""""""""""""""
class NivelAutoria(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Niveles de Autoria'
        verbose_name = 'Nivel de Autoria'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre


class NivelMES(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Niveles de MES'
        verbose_name = 'Nivel de MES'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad EVENTO
"""""""""""""""""""""""""""""""""""""""""""""""""""
class NivelEvento(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Niveles de Evento'
        verbose_name = 'Nivel de Evento'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class TipoPublicacion(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Tipos de publicación'
        verbose_name = 'Tipo de publicación'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad CAPACITACION
"""""""""""""""""""""""""""""""""""""""""""""""""""
class TipoCapacitacion(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Tipos de capacitación'
        verbose_name = 'Tipo de capacitación'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class RolCapacitación(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Roles de capacitación'
        verbose_name = 'Rol de capacitación'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class ModalidadCapacitacion(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Modalidades de capacitación'
        verbose_name = 'Modalidad de capacitación'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad PATENTE/ResultadoIntroducido
"""""""""""""""""""""""""""""""""""""""""""""""""""
class CienciaObra(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Ciencias de Obras'
        verbose_name = 'Ciencia de Obra'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class TipoObra(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Tipos de Obras'
        verbose_name = 'Tipo de Obra'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad ResultadoIntroducido
"""""""""""""""""""""""""""""""""""""""""""""""""""

class TamañoObra(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Tamaños de Obras'
        verbose_name = 'Tamaño de Obra'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad Premio
"""""""""""""""""""""""""""""""""""""""""""""""""""
class LugarPremio(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Lugares de Premios'
        verbose_name = 'Lugar de Premio'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre


class CaracterPremio(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Caracteres de Premios'
        verbose_name = 'Caracter de Premio'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad Empleo de Estudiantes
"""""""""""""""""""""""""""""""""""""""""""""""""""
class Fuente(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Fuentes de Empleo de estudiantes'
        verbose_name = 'Fuente de Empleo de estudiantes'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad Noticia
"""""""""""""""""""""""""""""""""""""""""""""""""""
class CaracterNoticia(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Caracteres de noticias'
        verbose_name = 'Caracter de noticia'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad Obra Cientifica
"""""""""""""""""""""""""""""""""""""""""""""""""""
class TipoObraCientifica(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Tipos de obras cientificas'
        verbose_name = 'Tipo de obra cientifica'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre   

"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad Proyecto IDi
"""""""""""""""""""""""""""""""""""""""""""""""""""

class NivelProyecto(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      class Meta:
        verbose_name_plural = 'Niveles de Proyectos'
        verbose_name = 'Nivel de Proyecto'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class LineaCientificaProyecto(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      class Meta:
        verbose_name_plural = 'Lineas Cientificas de Proyectos'
        verbose_name = 'Linea Cientifica de Proyecto'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class Area(models.Model):
      nombre = models.CharField(max_length=150, unique=True)
      descripcion = models.CharField(max_length=255)
      class Meta:
        verbose_name_plural = 'Areas'
        verbose_name = 'Area'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class Grupo(models.Model):
      nombre = models.CharField(max_length=150, unique=True)
      descripcion = models.CharField(max_length=255)
      area = models.ForeignKey(Area)
      class Meta:
        verbose_name_plural = 'Grupos'
        verbose_name = 'Grupo'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre


"""""""""""""""""""""""""""""""""""""""""""""""""""

Nomencladores para la entidad SAI
"""""""""""""""""""""""""""""""""""""""""""""""""""

class TipoSAISolicitado(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      class Meta:
        verbose_name_plural = 'Tipos de SAI'
        verbose_name = 'Tipo de SAI'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class SubTipoSAISolicitado(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      tipo = models.ForeignKey(TipoSAISolicitado)
      class Meta:
        verbose_name_plural = 'Sub Tipos de SAI'
        verbose_name = 'Sub Tipo de SAI'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre        

class TematicaSAI(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      class Meta:
        verbose_name_plural = 'Temáticas de SAI'
        verbose_name = 'Temática de SAI'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class PersonalRecibirSAI(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      class Meta:
        verbose_name_plural = 'Totales de personas a recibir SAI'
        verbose_name = 'Total de personas a recibir SAI'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class TiempoSAI(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      class Meta:
        verbose_name_plural = 'Tiempos SAI'
        verbose_name = 'Tiempo SAI'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class EvaluacionSAI(models.Model):
      nombre = models.CharField(max_length=255, unique=True)
      class Meta:
        verbose_name_plural = 'Evaluaciones de SAI'
        verbose_name = 'Evaluacion de SAI'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

"""""""""""""""""""""""""""""""""""""""""""""""""""

SAISA´s entities
"""""""""""""""""""""""""""""""""""""""""""""""""""

class Pais(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      class Meta:
        verbose_name_plural = 'Paises'
        verbose_name = 'Pais'
        ordering = ['nombre']
      def __str__(self):
        return u"%s" % self.nombre

class Ciudad(models.Model):
      nombre = models.CharField(max_length=128, unique=True)
      pais = models.ForeignKey(Pais)
      class Meta:
        verbose_name_plural = 'Ciudades'
        verbose_name = 'Ciudad'
        ordering = ['nombre']
      def __str__(self):
        return self.nombre                

class Continent(models.Model):
      continent_name = models.CharField(max_length=128, unique=True)
      poblation = models.CharField(max_length=128)
      class Meta:
        verbose_name_plural = 'Continentes'
        verbose_name = 'Continente'
      def __str__(self):
        return u"%s" % self.continent_name

class Country(models.Model):
      country_name = models.CharField(max_length=128, unique=True)
      poblation = models.CharField(max_length=128)
      continent = models.ForeignKey(Continent)
      class Meta:
        verbose_name_plural = 'Countries'
        verbose_name = 'Country'
      def __str__(self):
        return self.country_name        

class File(models.Model):


      MEDIA_CHOICES = (('Audio',(('vinyl', 'Vinyl'),('cd', 'CD'),)),('Video',(('vhs', 'VHS Tape'),('dvd', 'DVD'),)),('unknown', 'Unknown'),)
      item = models.CharField('Item name: ', max_length=128)
      image = models.ImageField(upload_to = 'FileSampleApp/')
      anyimage = AnyImageField(upload_to = 'FileSampleApp/',
                                 verbose_name='Any image field')
      File = models.FileField(upload_to = 'FileSampleApp/')
      year_in_school = models.CharField(max_length=20,
                                        choices=MEDIA_CHOICES,
                                        verbose_name='Years in school',
                                        default='vinyl')
      datetimefiel = models.DateField()
      gender = models.CharField(max_length=20,
                                        verbose_name='Gender')
      name = models.CharField(max_length=20, verbose_name='Name')
      continent = models.CharField(max_length=20, verbose_name='Continent')
      country = models.CharField(max_length=20, verbose_name='Country')
      # continent = models.ForeignKey(Continent)
      # country = ChainedForeignKey(
      #       Country, 
      #       verbose_name='country',
      #       chained_field="continent_name",
      #       chained_model_field="continent_name"
      #   )
      class Meta:
        verbose_name_plural = 'Files'
        verbose_name = 'File'
      def __str__(self):
        return self.item

@receiver(post_delete, sender=File)
def image_post_delete_handler(sender, **kwargs):
    FileSample = kwargs['instance']
    storage, path = FileSample.image.storage, FileSample.image.path
    storage.delete(path)

@receiver(post_delete, sender=File)
def file_post_delete_handler(sender, **kwargs):
    FileSample = kwargs['instance']
    storage, path = FileSample.File.storage, FileSample.File.path
    storage.delete(path)

# class CustomUser(AbstractBaseUser):
#     COUNTRIES = (
#     ('FR', 'Freshman'),
#     ('SO', 'Sophomore'),
#     ('JR', 'Junior'),
#     ('SR', 'Senior'),
#     )   # Contents are left as an exercise to the reader

#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     # Address
#     address1 = models.CharField(max_length=50)
#     address2 = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     country = models.CharField(max_length=50, choices=COUNTRIES)

#     # Contact
#     mobile = models.CharField(max_length=32)
#     home = models.CharField(max_length=32)
#     office = models.CharField(max_length=32)
#     twitter = models.CharField(max_length=100)

#     def __unicode__(self):
#         return self.username
only_letters = RegexValidator(r'^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')

class Publicacion(models.Model):
      propietario = models.ForeignKey(User)
      #propietario = models.CharField(max_length=128,verbose_name='Propietario:',db_column='Propietario')
      titulo = models.CharField(max_length=255,verbose_name='Titulo:',db_column='Titulo',validators=[alpha])
      #autor = models.CharField(max_length=128,verbose_name='Autor:',db_column='Autor')
      autores = models.ManyToManyField(User, db_table=u'Publicacion_Autores', related_name='Publicacion_Autores')
      #nivel_autoria = models.ForeignKey(NivelAutoria)
      # cambiar el tipo de field de año     
      anno = models.CharField(max_length=10,verbose_name='Año:',db_column='Anno')
      pais = models.ForeignKey(Pais)
      ciudad = models.ForeignKey(Ciudad)
      editorial = models.CharField(max_length=50,verbose_name='Editorial:',db_column='Editorial',validators=[alpha])
      publicacion = models.CharField(max_length=100,verbose_name='Publicación:',db_column='Publicacion',validators=[alpha])
      numero = models.PositiveIntegerField(max_length=10,verbose_name='Número:',db_column='Numero')
      volumen = models.PositiveIntegerField(max_length=10,verbose_name='Volúmen:',db_column='Volumen')
      nivel_mes = models.ForeignKey(NivelMES)
      aprobacion = models.BooleanField(max_length=1000,verbose_name='Aprobacion:',db_column='Aprobacion',default='False')
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/Publicacion')
      
      class Meta:
        verbose_name_plural = 'Publicaciones'
        verbose_name = 'Publicacion'
      def __str__(self):
        return self.titulo   
      def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.fichero.url,)
        else:
            return "No attachment"
      file_link.allow_tags = True


@receiver(post_delete, sender=Publicacion)
def image_post_delete_handler_publicacion(sender, **kwargs):
      publicacion = kwargs['instance']
      storage, path = publicacion.fichero.storage, publicacion.fichero.path
      storage.delete(path)    

class Evento(models.Model):
      nombre = models.CharField(max_length=255,verbose_name='Nombre:',db_column='Nombre',validators=[alpha])
      edicion = models.PositiveIntegerField(max_length=10,verbose_name='Número de la edición:',db_column='Edicion')
      nivel = models.ForeignKey(NivelEvento)
      pais = models.ForeignKey(Pais)
      ciudad = models.ForeignKey(Ciudad)
      tipo_publicacion = models.ForeignKey(TipoPublicacion)
      issn = models.CharField(max_length=20,verbose_name='ISSN:',db_column='ISSN')
      
      
      class Meta:
        verbose_name_plural = 'Eventos'
        verbose_name = 'Evento'
      def __str__(self):
        return self.nombre


class PonenciaEvento(models.Model):
      propietario = models.ForeignKey(User)
      titulo = models.CharField(max_length=255,verbose_name='Título:',db_column='Titulo',validators=[alpha])
      evento = models.ForeignKey(Evento)
      # autor = models.CharField(max_length=20,verbose_name='Autor:',db_column='Autor')
      # nivel_autoria = models.ForeignKey(NivelAutoria)
      autores = models.ManyToManyField(User, db_table=u'PonenciaEvento_Autores', related_name='PonenciaEvento_Autores')
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/PonenciaEvento')
      
      
      class Meta:
        verbose_name_plural = 'Ponencias en eventos'
        verbose_name = 'Ponencia en evento'
      def __str__(self):
        return self.titulo
      def getEventId(self):
        return self.evento.id
      def getEventName(self):
        return self.evento.nombre

@receiver(post_delete, sender=PonenciaEvento)
def image_post_delete_handler_ponenciaevento(sender, **kwargs):
      ponenciaevento = kwargs['instance']
      storage, path = ponenciaevento.fichero.storage, ponenciaevento.fichero.path
      storage.delete(path)


class ProyectoiDi(models.Model):
      propietario = models.ForeignKey(User, related_name="propietarioProyectoIDi")
      titulo = models.CharField(max_length=255,verbose_name='Título:',db_column='Titulo')
      nivel = models.ForeignKey(NivelProyecto)
      area_ejecutora = models.ForeignKey(Area)
      linea_cientifica = models.ForeignKey(LineaCientificaProyecto)
      #nombre = models.ForeignKey(Evento)
      #rol = models.CharField(max_length=255,verbose_name='Rol:',db_column='Rol')
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/ProjectoIdi')   
      #photos = SortedManyToManyField(Publicacion)
      #publicaciones = models.ManyToManyField(Publicacion, db_table=u'Publications_To_Projects')
      #Cannot specify a db_table if an intermediary model is used.
      #participantes = models.ManyToManyField(User, through='Membresia')
      miembros = models.ManyToManyField(User, db_table=u'ProyectoIDI_Miembros', related_name='ProyectoIDI_Miembros')
      
      class Meta:
        verbose_name_plural = 'Proyectos IDi'
        verbose_name = 'Proyecto IDi'
      def __str__(self):
        return self.titulo


@receiver(post_delete, sender=ProyectoiDi)
def image_post_delete_handler_proyectoIDi(sender, **kwargs):
      proyectoIDi = kwargs['instance']
      storage, path = proyectoIDi.fichero.storage, proyectoIDi.fichero.path
      storage.delete(path)

from django.core.exceptions import NON_FIELD_ERRORS


class Membresia(models.Model):
    participantes = models.ForeignKey(User)
    proyectoIDi = models.ForeignKey(ProyectoiDi)
    rol = models.CharField(max_length=64)
    class Meta:
        unique_together = ('participantes', 'proyectoIDi')
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        # }

class Membership(models.Model):
    participantes = models.ForeignKey(User)
    proyectoIDi = models.ForeignKey(ProyectoiDi)
    rol = models.CharField(max_length=64)
    estado = models.CharField(max_length=64)
    class Meta:
        unique_together = ('participantes', 'proyectoIDi')
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        # }

class Capacitacion(models.Model):
      propietario = models.ForeignKey(User)
      nombre = models.CharField(max_length=255,verbose_name='Nombre:',db_column='Nombre',validators=[alpha])
      tipo = models.ForeignKey(TipoCapacitacion)
      fecha = models.DateField()
      rol = models.ForeignKey(RolCapacitación)
      modalidad = models.ForeignKey(ModalidadCapacitacion)
      institucion = models.CharField(max_length=255,verbose_name='Institución:',db_column='Institucion',validators=[alpha])
      pais = models.ForeignKey(Pais)
      ciudad = models.ForeignKey(Ciudad)
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/Capacitacion')   
      estudiantes = models.ManyToManyField(User, db_table=u'Item_Capacitacion_Estudiantes', related_name='Estudiantes_Capacitacion')
      profesores = models.ManyToManyField(User, db_table=u'Item_Capacitacion_Profesores' , related_name='Profesores_Capacitacion')
      class Meta:
        verbose_name_plural = 'Capacitaciones'
        verbose_name = 'Capacitacion'
      def __str__(self):
        return self.nombre     

@receiver(post_delete, sender=Capacitacion)
def image_post_delete_handler_capacitacion(sender, **kwargs):
      capacitacion = kwargs['instance']
      storage, path = capacitacion.fichero.storage, capacitacion.fichero.path
      storage.delete(path)                     

class ObraCientifica(models.Model):
      propietario = models.ForeignKey(User, related_name="propietario_ObraCientifica")
      titulo = models.CharField(max_length=128,verbose_name='Título', unique=True, db_column='Titulo',validators=[alpha])
      tipo_obra = models.ForeignKey(TipoObraCientifica)
      fecha_creacion = models.DateField(verbose_name='Fecha de creación', )
      autores = models.ManyToManyField(User, db_table=u'ObraCientifica_Autores')
      descripcion = models.CharField(max_length=255,verbose_name='Descripción', db_column='Descripcion',validators=[comment])
      tamanno = models.ForeignKey(TamañoObra)
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Adjunto', upload_to = 'FileSampleApp/ObraCientifica')   
      class Meta:
        verbose_name_plural = 'Obras cientificas'
        verbose_name = 'Obra cientifica'
        ordering = ['titulo']
      def __str__(self):
        return u"%s" % self.titulo 

@receiver(post_delete, sender=ObraCientifica)
def image_post_delete_handler_ObraCientifica(sender, **kwargs):
    ObraCientifica = kwargs['instance']
    storage, path = ObraCientifica.fichero.storage, ObraCientifica.fichero.path
    storage.delete(path)
	  
class Patente(models.Model):
      propietario = models.ForeignKey(User)
      nombre_obra = models.ForeignKey(ObraCientifica)
      ciencia_obra = models.ForeignKey(CienciaObra)
      fecha = models.DateField()
      tipo_obra = models.ForeignKey(TipoObraCientifica)
      fuente_registro = models.CharField(max_length=100,verbose_name='Fuente:',db_column='Fuente')
      cantidad_autores = models.IntegerField(max_length=3,verbose_name='Cantidad de autores:',db_column='Cantidad_Autores')
      propietarios = models.ManyToManyField(User, db_table=u'Patente_Propietarios', related_name='Patente_Propietarios')
      comentario = models.CharField(max_length=255,verbose_name='Comentario:',db_column='Comentario',validators=[comment])
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/Patente')   
      
      class Meta:
        verbose_name_plural = 'Patentes'
        verbose_name = 'Patente'
      def __str__(self):
        return self.nombre_obra   

@receiver(post_delete, sender=Patente)
def image_post_delete_handler_patente(sender, **kwargs):
      patente = kwargs['instance']
      storage, path = patente.fichero.storage, patente.fichero.path
      storage.delete(path)                              


class ResultadoIntroducido(models.Model):
      propietario = models.ForeignKey(User)
      nombre_obra = models.ForeignKey(ObraCientifica)
      ciencia_obra = models.ForeignKey(CienciaObra)
      fecha = models.DateField()
      tipo_obra = models.ForeignKey(TipoObraCientifica)
      tamanno = models.ForeignKey(TamañoObra)
      # tipo_obra = models.CharField(max_length=20,verbose_name='Tipo de obra:',db_column='Tipo_Obra')
      institucion = models.CharField(max_length=255,verbose_name='Institución donde se introdujo:',db_column='Institucion',validators=[alpha])
      cantidad_autores = models.IntegerField(max_length=3,verbose_name='Cantidad de autores:',db_column='Cantidad_Autores')
      comentario = models.CharField(max_length=255,verbose_name='Comentario:',db_column='Comentario',validators=[comment])
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/ResultadoIntroducido')   
      
      class Meta:
        verbose_name_plural = 'Patentes'
        verbose_name = 'Patente'
      def __str__(self):
        return self.nombre_obra

@receiver(post_delete, sender=ResultadoIntroducido)
def image_post_delete_handler_resultadointroducido(sender, **kwargs):
      resultadointroducido = kwargs['instance']
      storage, path = resultadointroducido.fichero.storage, resultadointroducido.fichero.path
      storage.delete(path) 


class Premio(models.Model):
      propietario = models.ForeignKey(User)
      titulo = models.CharField(max_length=255,verbose_name='Título:',db_column='Titulo',validators=[alpha])
      autores = models.ManyToManyField(User, db_table=u'Premio_Autores', related_name='Premio_Autores')
      publicacion = models.ForeignKey(Publicacion, null=True, verbose_name='Publicación a premiar:')
      ponenciaevento = models.ForeignKey(PonenciaEvento, null=True, verbose_name='Ponencia a premiar:')
      proyecto = models.ForeignKey(ProyectoiDi, null=True, verbose_name='Proyecto a premiar:')
      obracientifica = models.ForeignKey(ObraCientifica, null=True, verbose_name='Obra Científica a premiar:')
	  # autor = models.CharField(max_length=255,verbose_name='Autor:',db_column='Autor')
      # nivel_autoria = models.ForeignKey(NivelAutoria)
      anno = models.PositiveIntegerField(max_length=4,verbose_name='Año:',db_column='Anno',default=1,
        validators=[
            MaxValueValidator(3000),
            MinValueValidator(1)
        ])
      pais = models.ForeignKey(Pais)
      ciudad = models.ForeignKey(Ciudad)
      lugar_premio = models.ForeignKey(LugarPremio)
      nivel_premio = models.ForeignKey(NivelEvento)
      caracter = models.ForeignKey(CaracterPremio)
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/Premio')   
      
      class Meta:
        verbose_name_plural = 'Premios'
        verbose_name = 'Premio'
      def __str__(self):
        return self.titulo


@receiver(post_delete, sender=Premio)
def image_post_delete_handler_premio(sender, **kwargs):
      premio = kwargs['instance']
      storage, path = premio.fichero.storage, premio.fichero.path
      storage.delete(path)       

class EmpleoEstudiantes(models.Model):
      propietario = models.ForeignKey(User, related_name="propietario")
      # fuente = models.ForeignKey(Fuente)
      # nombre_fuente = models.CharField(max_length=150,verbose_name='Nombre de la Fuente:',db_column='Nombre_Fuente')
      # nombre_obra = models.ForeignKey(ObraCientifica)
      publicacion = models.ForeignKey(Publicacion, null=True, verbose_name='Publicacion a emplear:')
      ponenciaevento = models.ForeignKey(PonenciaEvento, null=True, verbose_name='Ponencia a emplear:')
      proyecto = models.ForeignKey(ProyectoiDi, null=True, verbose_name='Proyecto a emplear:')
      obracientifica = models.ForeignKey(ObraCientifica, null=True, verbose_name='Obra Científica a emplear:')
      cantidad_estudiantes = models.CharField(max_length=10,verbose_name='Cantidad de estudiantes:',db_column='Cantidad_Estudiantes')
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Asociado', upload_to = 'FileSampleApp/EmpleoEstudiantes')   
      estudiantes = models.ManyToManyField(User, db_table=u'Employed_Users')
    
      class Meta:
        verbose_name_plural = 'Empleo de Estudiantes'
        verbose_name = 'Empleo de Estudiante'
      def __str__(self):
        return self.propietario

@receiver(post_delete, sender=EmpleoEstudiantes)
def image_post_delete_handler_EmpleoEstudiantes(sender, **kwargs):
      EmpleoEstudiantes = kwargs['instance']
      storage, path = EmpleoEstudiantes.fichero.storage, EmpleoEstudiantes.fichero.path
      storage.delete(path)      


class Noticia(models.Model):
      propietario = models.ForeignKey(User)
      titular = models.CharField(max_length=255,verbose_name='Titular:',db_column='Titular', unique=True,validators=[alphanumeric])
      rango_tiempo = models.CharField(max_length=150,verbose_name='Rango de Tiempo:',db_column='Rango de Tiempo')
      publicacion = models.DateField(verbose_name='Publicación:')
      tiempo_visibilidad = models.CharField(max_length=10,verbose_name='Tiempo de visibilidad:',db_column='Tiempo_Visibilidad')
      caracter = models.ForeignKey(CaracterNoticia)
      contenido = models.CharField(max_length=2555,verbose_name='Contenido:',db_column='Contenido_Noticia')
      aprobacion = models.BooleanField(max_length=1000,verbose_name='Aprobacion:',db_column='Aprobacion',default='False')
      fichero = models.FileField(max_length=255,verbose_name='Asociar fichero',db_column='Direccion_Fichero_Adjunto', upload_to = 'FileSampleApp/Noticia')   
      
      class Meta:
        verbose_name_plural = 'Noticias'
        verbose_name = 'Noticia'
      def __str__(self):
        return self.titular


@receiver(post_delete, sender=Noticia)
def image_post_delete_handler_EmpleoEstudiantes(sender, **kwargs):
      Noticia = kwargs['instance']
      storage, path = Noticia.fichero.storage, Noticia.fichero.path
      storage.delete(path)   

class SAI(models.Model):
    area_solicitante = models.CharField(max_length=255,db_column='Area_solicitante',validators=[alpha])
    fecha = models.DateField()
    codigo = models.CharField(verbose_name='Código:', max_length=255,validators=[numeric])
    # Datos del solicitante
    solicitante = models.ForeignKey(User, related_name="Solicitante SAI")
    nombre_solicitante = models.CharField(null=True, max_length=255)
    cargo_solicitante = models.CharField(null=True, max_length=255)
    solapin_solicitante = models.CharField(null=True, max_length=255)
    telefono_solicitante = models.PositiveIntegerField(null=True, max_length=255)
    email_solicitante = models.EmailField(null=True, max_length=255)
    # Fin Datos del solicitante
    tipo_SAI = models.ForeignKey(TipoSAISolicitado)
    subtipo_SAI = models.ForeignKey(SubTipoSAISolicitado)
    personal_SAI = models.ForeignKey(PersonalRecibirSAI)
    tematica_SAI = models.ForeignKey(TematicaSAI)
    tiempo_SAI = models.ForeignKey(TiempoSAI)
    descripcion_SAI = models.CharField(max_length=255, verbose_name='Descripción:',validators=[comment])
    # Aprobacion
    aprobacion = models.NullBooleanField(null=True, max_length=1000,verbose_name='Aprobacion:',db_column='Aprobacion',default='False')
    aprobador_SAI = models.ForeignKey(User, related_name="Aprobador SAI", null=True)
    aprobador_cargo_SAI = models.CharField(null=True, max_length=255,validators=[alpha])
    responsable_ejecucion_SAI = models.ForeignKey(User, related_name="Responsable Ejecucion SAI", verbose_name='Responsable ejecución SAI:', null=True)
    comentario_SAI_No_Aprobacion = models.CharField(null=True, max_length=255, verbose_name='Comentar la no aprobación:',validators=[comment])
    # Fin Aprobacion
    # Evaluacion
    evaluacion_SAI = models.ForeignKey(EvaluacionSAI, null=True, verbose_name='Evaluación:')
    comentario_SAI_evaluacion = models.CharField(null=True, max_length=255, verbose_name='Comentar evaluación:',)
    # Fin Evaluacion
    ejecutores = models.ManyToManyField(User, db_table=u'Ejecutores_SAI')
    class Meta:
      verbose_name_plural = 'SAIs'
      verbose_name = 'SAI'
      ordering = ['area_solicitante']
      def __str__(self):
        return u"%s" % self.area_solicitante

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='perfil')
    solapin = models.CharField(max_length=128, unique=True, db_column='Numero_Solapin', default="0") 
    expediente = models.PositiveIntegerField(max_length=10,verbose_name='Expediente:',db_column='ID_Expediente', default=0)
    sexo = models.ForeignKey(Sexo, default=0)
    edad = models.CharField(max_length=10, db_column='Edad', default=0)  
    direccion = models.CharField(max_length=255, db_column='Direccion_Particular', default=0)  
    provincia = models.ForeignKey(Provincia, default=0)
    municipio = models.ForeignKey(Municipio, default=0)
    carne_identidad = models.CharField(max_length=255, db_column='Carne_Identidad', default=0) 
    cargo = models.ForeignKey(Cargo, default=0)
    categoria_docente = models.ForeignKey(CategoriaDocente, default=0)
    grado_cientifico = models.ForeignKey(GradoCientifico, default=0)
    especialidad_graduado = models.CharField(max_length=144, db_column='Especialidad_Graduado', default="0")  
    anno_graduado = models.DateField(default=0)
    titulo_academico = models.ForeignKey(TituloAcademico, default=0)
    rol_saisa = models.ForeignKey(Rol, default=0)
    grupo = models.ForeignKey(Grupo, default=0)

class ModeloYoamel(models.Model):
      href = models.CharField(max_length=128,verbose_name='href (Relacionado con):',db_column='href')
      data_largesrc = models.ImageField(upload_to = 'FileSampleApp/Yoamel',db_column='data_largesrc')
      data_title = models.CharField(max_length=255,verbose_name='data_title (Titulo):',db_column='data_title')
      data_description = models.CharField(max_length=255,verbose_name='data_description (Descripción):',db_column='data_description')
      img = models.ImageField(upload_to = 'FileSampleApp/Yoamel',db_column='Img')
      
      class Meta:
        verbose_name_plural = 'Modelos Yoamel'
        verbose_name = 'Modelo Yoamel'
      def __str__(self):
        return self.data_title      