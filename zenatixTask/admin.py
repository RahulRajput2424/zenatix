from django.contrib import admin
from zenatixTask.models import *


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','unit','price']

admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(IngredientProduct)
admin.site.register(OrderDetails)

