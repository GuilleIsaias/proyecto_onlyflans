from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import Contact_Form
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(flan_is_private=False)
    return render(request, 'index.html', {'flanes_publicos': flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

def exito(request):
    return render(request, 'exito.html', {})

def welcome(request):
    flanes_privados = Flan.objects.filter(flan_is_private=True)
    return render(request, 'welcome.html', {'flanes_privados': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)

        if form.is_valid():
            contacto_form= ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = Contact_Form()

    return render(request, 'contacto.html', {'form': form})


