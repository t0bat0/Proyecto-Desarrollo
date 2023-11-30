from django.shortcuts import render, get_object_or_404, redirect
from .models import Presupuesto, Cliente, Producto
from .models.presupuesto import PresupuestoProducto
from django.http import HttpResponse, JsonResponse
from .forms.cliente_forms import CrearCliente
from .forms.presupuesto_forms import  CrearPresupuestoVacio, AgregarProductoForm
from django.views import generic
from .forms import presupuesto_forms
from .forms.login_forms import CustomLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
from django.template.loader import render_to_string
import tempfile
from weasyprint  import HTML





@login_required(login_url='/iniciar-sesion/')
def crear_cliente(request):
    if request.method == 'GET':
        return render(request, "presupuesto/crear-cliente.html", {
        'form': CrearCliente
    })
    else:
        Cliente.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                               domicilio=request.POST['domicilio'],
                               telefono=request.POST['telefono'], email=request.POST['email'])
        """
        pp=PresupuestoProducto()
        pp.producto=p
        pp.Presupuesto=pp1
        pp.cantidad=2
        pp.save()
        """

        return redirect('/')


def project_list(request):
    return render(request, "presupuesto/project-list.html")


def elegir(request):
    presupuestos = Presupuesto.objects.all()
    busqueda = request.GET.get('busqueda')
    if busqueda == None:
        busqueda=''
    if busqueda:
        presupuestos = presupuestos.filter(nombre__icontains=busqueda)
    return render(request, "presupuesto/elegir-presupuesto.html", {'pre': presupuestos, 'busqueda': busqueda})


def eliminiar_producto(request, slug_presupuesto, producto_id):
    presupuesto = get_object_or_404(Presupuesto, slug=slug_presupuesto)
    producto = get_object_or_404(Producto, id=producto_id)

    if producto in presupuesto.id_producto.all():
        presupuesto.id_producto.remove(producto)
        return redirect('/presupuesto/' + slug_presupuesto)
    else:
        return HttpResponse("No se puede eliminar el producto porque no está en el presupuesto")


@login_required(login_url='/iniciar-sesion/')
def project_detail(request, slug_presupuesto):
    presupuesto = get_object_or_404(Presupuesto, slug=slug_presupuesto)
    presupuesto_productos = PresupuestoProducto.objects.filter(
        presupuesto=presupuesto)
    #print(presupuesto_productos[0].alto)
    total = sum(producto.subtotal() for producto in presupuesto_productos)
    cantida_productos = presupuesto_productos.count()


    if request.method == 'POST' and 'producto_id' in request.POST:
        producto_id = request.POST['producto_id']
        producto = Producto.objects.get(pk=producto_id)
        presupuesto.id_producto.remove(producto)
        return JsonResponse({"message": "Producto eliminado exitosamente"})

    if request.method == 'POST':
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            producto_cantidad = form.cleaned_data['producto_cantidad']
            producto = form.cleaned_data['producto']
            
            # Crea el PresupuestoProducto
            presupuesto_producto = form.save(commit=False)
            presupuesto_producto.presupuesto = presupuesto
            presupuesto_producto.producto = producto
            presupuesto_producto.precio_producto = producto.precio_producto
            presupuesto_producto.save()
          
            # Usa el método set() para establecer la relación many-to-many
            presupuesto_producto.id_accesorio.set(form.cleaned_data['id_accesorio'])
            #print(presupuesto_producto.id_accesorio.all())
            return redirect('/presupuesto/' + slug_presupuesto)

    else:
        form = AgregarProductoForm()

    return render(request, 'presupuesto/detalle-presupuesto.html', {'form': form, 'presupuesto': presupuesto, 'total': total, 'cantida_productos': cantida_productos,'productopresupuesto':presupuesto_productos})



   
@login_required(login_url='/iniciar-sesion/')    
def crear_presupuesto(request):
    if request.method =="GET":
        return render(request,"presupuesto/crear-presupuesto.html",{
        'form': CrearPresupuestoVacio()
    })
    else:
        
        cliente2 = Cliente.objects.get(pk=request.POST['id_cliente'])
        Presupuesto.objects.create(nombre=request.POST['nombre'],id_cliente=cliente2,)
        return redirect('/elegir/')
        

def iniciar_sesion(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.GET)
                next_url = request.GET  ['next']
                return redirect(next_url)
    else:
        form = CustomLoginForm()

    return render(request, 'presupuesto/log-in.html', {'form': form})





@login_required(login_url='/iniciar-sesion/')
def crear_presupuesto_pdf(request, slug_presupuesto):
    print(slug_presupuesto)
    presupuesto = get_object_or_404(Presupuesto, slug=slug_presupuesto)
    presupuestoproducto = PresupuestoProducto.objects.filter(presupuesto=presupuesto)
    print(presupuesto)
    total = sum(producto.subtotal() for producto in presupuestoproducto )

    # Create the response object
    response = HttpResponse(content_type='application/pdf')

    # Set the response headers
    response['Content-Disposition'] = 'inline; attachment; filename=Expenses' + str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    # Render the HTML template
    html_string = render_to_string('presupuesto/pdf-output.html', 
        {'presupuesto': presupuesto, 
        'productopresupuesto':presupuestoproducto,
        'total':int(total)
        })

    # Create the PDF content
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Write the PDF content to a temporary file
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        # Create a separate file handle for reading
        with open(output.name, 'rb') as read_file:
            # Write the PDF content to the response
            response.write(read_file.read())

    # Return the response
    return response


