from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'bra': 'Hkwekwekwe'
    }
    return render(request, 'index.html', context)