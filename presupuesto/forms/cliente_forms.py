from django import forms
from ..models import Cliente


#class ProductoWidget(s2forms.ModelSelect2Widget):
   # search_fields = [
      #  "nombre__icontains",
      #  "descripcion__icontains",
   # ]

class CrearCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','domicilio','telefono','email']
        widgets = { 'nombre': forms.TextInput(attrs={ 'style': 'color: aliceblue;'}),
                    'apellido': forms.TextInput(attrs={ 'style': 'color: aliceblue;'}),
                    'domicilio': forms.TextInput(attrs={ 'style': 'color: aliceblue;'}),
                    'telefono': forms.TextInput(attrs={ 'style': 'color: aliceblue;'}),
                    'email': forms.EmailInput(attrs={ 'style': 'color: aliceblue;'}),
                    }
    #class Meta:
      #  model = models.Cliente
      #  fields = "__all__"
       # widgets = {
      #      "lalala": ProductoWidget,
      #  }