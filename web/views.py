from django.shortcuts import render, reverse, redirect
from django.views.generic import FormView
from .models import Flan, ContactForm
from .forms import Contact_Form, Contactillo
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





