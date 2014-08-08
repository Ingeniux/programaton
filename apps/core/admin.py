from django import forms
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from apps.core.models import *


class TorneoAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'fecha_inicio', 'fecha_finalizacion']
	list_filter = ['fecha_inicio']

class ProblemaAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'dificultad']
	list_filter = ['torneo', 'dificultad']

class FrikiAdmin(admin.ModelAdmin):
	list_display = ['id', 'alias']
	list_filter = ['torneo']

class EstadoAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'descripcion']

class LenguajeAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre']

class Caso_de_PruebaAdmin(admin.ModelAdmin):
	list_display = ['problema', 'entrada', 'salida']

class SolucionAdmin(admin.ModelAdmin):
	list_display = ['id',  'torneo', 'problema', 'estado', 'fecha_envio']
	list_filter = ['torneo', 'estado']

admin.site.register(Torneo, TorneoAdmin)
admin.site.register(Problema, ProblemaAdmin)
admin.site.register(Friki, FrikiAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Lenguaje, LenguajeAdmin)
admin.site.register(Caso_de_Prueba, Caso_de_PruebaAdmin)
admin.site.register(Solucion, SolucionAdmin)


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Friki

    def clean_password(self):
        return self.initial["password"]


"""


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
"""
