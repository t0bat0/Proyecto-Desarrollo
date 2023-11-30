from django.contrib import admin


from ..models.producto import Producto, Accesorio


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","descripcion","alto","ancho")
    search_fields = ("nombre", "alto", "ancho")

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display=("nombre","descripcion","precio_accesorio")
    search_fields = ("nombre", "precio_accesorio")








    