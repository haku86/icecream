from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView


from braces.views import LoginRequiredMixin

from .models import Flavour
from .forms import FlavourCreateForm, FlavourUpdateForm, ScoopsUpdateForm

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

def flavour_list_view(request):
    flavours = Flavour.objects.all()

    if request.method == "POST":
        flavour_id = int(request.POST.get('flavour_id'))
        flavour = get_object_or_404(Flavour, pk=flavour_id)
        if 'one' in request.POST:
            flavour.scoops_remaining -= 1
            flavour.save()
        elif 'two' in request.POST:
            flavour.scoops_remaining -= 2
            flavour.save()
        return HttpResponseRedirect('/')  
    else:
        scoops_update_form = ScoopsUpdateForm()
    return render(request, 'index.html',{'flavours' : flavours, 'scoops_update_form' : scoops_update_form})

class FlavourCreateView(LoginRequiredMixin, FlavourActionMixin, CreateView):
    model = Flavour
    form_class = FlavourCreateForm
    action = "created"

class FlavourUpdateView(LoginRequiredMixin, FlavourActionMixin, UpdateView):
    model = Flavour
    form_class = FlavourUpdateForm
    action = "updated"

class FlavourDetailView(DetailView):
    model = Flavour