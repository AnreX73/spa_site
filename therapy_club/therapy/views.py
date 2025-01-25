from django.shortcuts import render
from therapy.forms import UserCreationForm


def index(request):
    form = UserCreationForm
    context = {
        'title': 'Therapy Club',
        'form': form

    }
    return render(request, 'therapy/index.html', context)
