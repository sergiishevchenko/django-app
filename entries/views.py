from django.shortcuts import render
from .models import Entry


def index(request):
    return render(request, 'entries/index.html')


def add(request):
    entries = Entry.objects.all()

    context = {'entries': entries}

    return render(request, 'entries/add.html', context)
