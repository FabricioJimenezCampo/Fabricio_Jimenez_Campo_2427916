from django.http import HttpResponse

def Pagina(recuest):
    return HttpResponse("Dato1")

def opcion(recuest):
    return HttpResponse("Dato2")
# Create your views here.
