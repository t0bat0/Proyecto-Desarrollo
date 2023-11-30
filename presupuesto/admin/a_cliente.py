from django.contrib import admin


from ..models.cliente import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","domicilio","telefono","email")
    search_fields = ("nombre", "apellido", "domicilio", "telefono", "email")


    
