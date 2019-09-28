from django.shortcuts import render, HttpResponse
from .forms import ClientesForm
#En este se definen las vistas de una app
#HttpResponse, sirve para ocupar comandos de html

# Create your views here.
#ul ---Menú html
#li --- lista
#a --- enlace

#Creamos una portada base
#html_base = """
#<h1>Mi web personal</h1>
#<ul>
#    <li><a href="/">Portada</a></li>
#    <li><a href="/about-me">Acerca de</a></li>
#    <li><a href="/portfolio">Portafolio</a></li>
#    <li><a href="/contac">Contacto</a></li>
#</ul>
#"""

def visitas(request):
    return render(request, "core/visitas.html") #Instrucción que manda a llamar la plantilla 

def clientes(request):
    cliente_form = ClientesForm()
    return render(request, "core/clientes.html", {'form': cliente_form})

def compras(request):
    return render(request, "core/compras.html")

#Para poder mandar un correo <a href="email">email</a> y es un ejemplo sin el uso de plantillas
#def contac(request):
 #   return HttpResponse(html_base + """
  #     <h2>Contacto</h2>
   #    <p>Aqui les dejo mi email para preguntarme dudas: <a href="mailto:angel_perezh3@outlook.es">angel_perezh3@outlook.es</a>.</p>
    #""")

def ventas(request):
    return render(request, "core/ventas.html")

def reportes(request):
    return render(request, "core/reportes.html")

def login(request):
    return render(request, "core/login.html")