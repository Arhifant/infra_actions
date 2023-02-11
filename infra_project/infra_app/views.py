from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'infra_app/first_page.html'
    return render(request, template)


def second_page(request):
    return HttpResponse('А это вторая страница!')
