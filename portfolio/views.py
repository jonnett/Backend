from django.shortcuts import render

# Create your views here.
def portfolio_home(request):
    context ={
        'nombre': 'Pedro Suarez',
        'profesion':'Desarrollador Fullstack',
        'anios_experiencia': 8
    }
    return render(request, "home.html", context)

def portfolio_servicios(request):
    context = {
        'servicios' : [
            { 'nombre': 'Desarrollo Web', 'descripcion': 'Desarrollo de sitios web modernos.'},
            { 'nombre': 'Consultoria', 'descripcion': 'Se atienden consultas del tarot.'},
            { 'nombre': 'Arquitectura', 'descripcion': 'Se diseñan arquitecturas robustas.'}
        ]
    }
    return render(request, "servicios.html", context)