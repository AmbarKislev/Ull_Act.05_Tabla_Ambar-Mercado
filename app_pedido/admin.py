from django.contrib import admin

# Register your models here.
from .models import Pedido
#Registrar el modelo Pedido en el admin
admin.site.register(Pedido)
