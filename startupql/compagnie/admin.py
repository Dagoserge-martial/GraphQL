from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class VilleAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'name',
        'statut',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class TitreAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'name',
        'statut',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class EmployeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'ville',
        'titre',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'ville',
        'titre',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'name',
        'ville',
        'titre',
        'statut',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Ville, VilleAdmin)
_register(models.Titre, TitreAdmin)
_register(models.Employe, EmployeAdmin)
