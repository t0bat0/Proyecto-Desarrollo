from django.contrib import admin

from ..models.presupuesto import Presupuesto, PresupuestoProducto, PresupuestoProductoAccesorio


class presupuestoaccesorio_inline(admin.TabularInline):
    model = PresupuestoProductoAccesorio
    extra = 1
    verbose_name_plural = 'Accesorios'


class presupuestoproducto_inline(admin.TabularInline):
    model = PresupuestoProducto
    inlines = [presupuestoaccesorio_inline]
    extra = 1
    
#crear una columna personalizada para que pueda mostrar los accesorios relacionados

@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    search_fields=("nombre","id_cliente")
    inlines=[presupuestoproducto_inline]
    list_display=("nombre","id_cliente")
    search_fields=("nombre", "id_cliente")