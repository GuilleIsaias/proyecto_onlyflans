from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import FormView
from .models import Flan, ContactForm
from .forms import Contact_Form, Contactillo
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(flan_is_private=False)
    return render(request, 'index.html', {'flanes_publicos': flanes_publicos})

def about(request):
    return render(request, 'about.html', {})

def exito(request):
    return render(request, 'exito.html', {})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(flan_is_private=True)
    return render(request, 'welcome.html', {'flanes_privados': flanes_privados})

@login_required
def recipe_detail(request, id):
    flan = get_object_or_404(Flan, flan_id=id)
    return render(request, 'recipe_detail.html', {'flan': flan})

@login_required
def recipes(request):
    flanes = Flan.objects.all()
    return render(request, 'recipes.html', {'flanes':flanes})

def contacto(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)

        if form.is_valid():
            contacto_form= ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = Contact_Form()

    return render(request, 'contacto.html', {'form': form})

class ContactView(FormView):
    form_class = Contactillo
    template_name = "contactomodel.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("customer_email")
        subject = form.cleaned_data.get("customer_name")
        message = form.cleaned_data.get("message")

        return super(ContactView, self).form_valid(form)
    
    def post(self,request):
        form = Contactillo(request.POST)
        form.save()

        return redirect("/")





