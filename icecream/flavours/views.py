from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView


from braces.views import LoginRequiredMixin

from .models import Flavour
from .forms import FlavourCreateForm

# Create your views here.
class FlavourActionMixin(object):

    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NoteImplementedError(msg)

    def form_valid(self, form):
        flavour = form.save(commit=False)
        flavour.scoops_remaining = 40
        flavour.save()
        msg = "Flavour {0}!".format(self.action)
        messages.info(self.request, msg)
        return super(FlavourActionMixin, self).form_valid(form)

class FlavourList(ListView):
    model = Flavour

class FlavourCreateView(LoginRequiredMixin, FlavourActionMixin, CreateView):
    model = Flavour
    form_class = FlavourCreateForm
    action = "created"

class FlavourUpdateView(LoginRequiredMixin, FlavourActionMixin, UpdateView):
    model = Flavour
    action = "updated"

class FlavourDetailView(DetailView):
    model = Flavour

    