from django import forms


class CreatePresupuesto():
    Nombre = forms.CharField(label="Nombre del nuevo presupuesto", max_length=200)
    Cliente = forms.CharField(label="Cliente", max_length=200)
    

    