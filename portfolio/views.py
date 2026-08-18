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
    return render(request, "servicios.html")