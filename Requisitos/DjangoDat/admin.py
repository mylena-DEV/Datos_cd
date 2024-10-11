from django.contrib import admin
from .models import *

#Forma de crear un model en el admin
class DatosAdmin(admin.ModelAdmin):
    list_display= ('nombres','apellidos','direccion','telefono')
#Sirve para registrar el modelo original y el del admin
admin.site.register(Datos,DatosAdmin)

class ProductosAdmin(admin.ModelAdmin):
    #caracteristicas del admin
    #mostrar campos de los registros
    list_display= ('codigo','nombre','precio')
    #buscar por campo
    search_fields = ('nombre','precio')
    #crear filtros por campo
    list_filter = ('precio',)
    #ordenar por  campos(por defecto ascendente, el menos es descendente)
    ordering = ('-precio',)
    #registros por paginas(paginado)
    list_per_page = 3
    #campos de solo lectura
    readonly_fields = ('nombre',)
# Register your models here.
admin.site.register(Productos,ProductosAdmin)


class Lugar_NacimientoAdmin(admin.ModelAdmin):
    list_display = ('Ciudad_de_nacimiento',)
    search_fields = ('Ciudad_de_nacimiento',)
    list_filter =   ('Ciudad_de_nacimiento',)
    ordering = ('Ciudad_de_nacimiento',)
    list_per_page = 1
    readonly_fields = ('Ciudad_de_nacimiento',)
admin.site.register(Lugar_Nacimiento,Lugar_NacimientoAdmin)

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('Ciudad_Actual',)
    search_fields = ('Ciudad_Actual',)
    list_filter =   ('Ciudad_Actual',)
    ordering = ('Ciudad_Actual',)
    list_per_page = 1
    readonly_fields = ('Ciudad_Actual',)
    
admin.site.register(Ciudad,CiudadAdmin)