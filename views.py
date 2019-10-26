from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.models import Patient,Medecin
from .forms import PatientForm

from django.views.generic import TemplateView, ListView
from django.db.models import Q

"""def hello(request):
   
   return render(request, "hello.html", {})
"""

class Resultat(ListView):
   model = Medecin

   template_name = 'resultat.html'

   def get_queryset(self): 
        query = self.request.GET.get('search')
        object_list = Medecin.objects.filter(
            Q(nom__icontains=query) | Q(specialite__icontains=query)
        )
        return object_list
        #return Medecin.objects.filter(Q(nom__icontains='mez') | Q(nom__icontains='ah'))

def signup(request):
   if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
   else:
        form = UserCreationForm()
   return render(request, 'registration/signup.html', {
        'form': form
    })

def home(request):
   search_term = ''
   if 'search' is request.GET:
      search_term = request.GET['search']
      medecin = Medecin.objects.all()

      medecin = medecin.filter(nom=search_term)
   return render(request, "home.html", {})

def formulaire(request):

   form = PatientForm(request.POST or None)


   if form.is_valid(): 
      # Ici nous pouvons traiter les données du formulaire
      nom = form.cleaned_data['nom']
      prenom = form.cleaned_data['prenom']
      age = form.cleaned_data['age']
      dateNaissance = form.cleaned_data['dateNaissance']
      adresse = form.cleaned_data['adresse']

      form.save()
      envoi = True


   return render(request, "registration/formulaire.html", locals())

def profil(request,id):
   try:
      patient = Patient.objects.get(id=id)
   #patients = Patient.objects.all()
   except Patient.DoesNotExist:
      raise Http404
   return render(request,"profil.html", {
         'patient': patient
    })