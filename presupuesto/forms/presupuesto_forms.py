from django import forms
from  ..models import Cliente
from ..models.presupuesto import Presupuesto,PresupuestoProducto, PresupuestoProductoAccesorio  









class CrearPresupuestoVacio(forms.ModelForm):
    class Meta:
        model= Presupuesto
        fields = ['nombre','id_cliente']
        widgets = { 
                   'nombre': forms.TextInput(attrs={ 'style': 'color: aliceblue;'}),
                   'id_cliente': forms.Select(attrs={ 'style': 'color: black;'}),
                   } 
        labels= {
            "id_cliente": "Cliente"
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['id_cliente'].widget.attrs = self.fields['id_cliente'].widget.attrs | {
            'style': 'color: aliceblue;'
        }              
    #id_cliente=forms.ModelChoiceField(queryset=Cliente.objects.all(),widget=forms.Select(attrs={ 'style': 'color: aliceblue;'}))

    
class AgregarProductoForm(forms.ModelForm):
  

    class Meta:
        model = PresupuestoProducto
        fields = ['producto', 'producto_cantidad', 'profundidad', 'alto', 'ancho', 'tipo_de_terminacion', 'id_accesorio']
        labels= {
            "id_accesorio": "Accesorios"
        }
        widgets = {'producto': forms.Select(attrs={'style': 'color: black'})}
        
        #'id_accesorio': forms.Select(attrs={'style': 'color: black;'})}
       #widgets = { 'producto': forms.TextInput(attrs={ 'style': 'color: aliceblue;'}),'producto_cantidad': forms.NumberInput(attrs={ 'style': 'color: bka;'}),  }    
        
        
