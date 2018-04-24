from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm
# Create your views here.
def index(request):
    entries = Entry.objects.all()
    return render(request, "calapp/index.html",{'entries':entries})

def details(request):
    entry = Entry.objects.get(id)
    return render(request, "calapp/details.html",{'entry':entry})

def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            ###
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name=name,
                date=date,
                description=description,
            ).save()

            return HttpResponseRedirect('/')
    else:
        form = EntryForm()
    return render(request, "calapp/form.html", {'form': form})
