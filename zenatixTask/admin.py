from django.contrib import admin
from zenatixTask.models import Ingredient, User


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','unit','price']

admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(User)
