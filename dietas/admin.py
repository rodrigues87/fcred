from django.contrib import admin

from dietas.models import Dieta


class DietaAdmin(admin.ModelAdmin):
    filter_horizontal = ('alimentos',)


admin.site.register(Dieta, DietaAdmin)
