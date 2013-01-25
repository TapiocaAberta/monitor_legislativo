# Create your views here.
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Projetos politicos!!')