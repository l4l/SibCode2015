import random
import string

from CellManager.parser import XML
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
import os


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def miss(request):
    return HttpResponse('404')


def load(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for key in request.FILES.keys():
                return HttpResponseRedirect(handle_uploaded_file(request.FILES[key]))

    else:
        form = UploadFileForm()
    return render_to_response('', {'form': form})


def handle_uploaded_file(file):
    file_name = random_string(10)
    while not os.path.isfile(file):
        file_name = random_string(10)

    destination = open(file_name, 'wb+')

    for chunk in file.chunks():
        destination.write(chunk)

    destination.close()
    update_file(file)


def update_file(file):
    xml = XML(file)
    xml.eval()
    xml.save(file)


def random_string(n):
    return ''.join(random
                   .SystemRandom()
                   .choice(string.ascii_uppercase + string.digits)
                   for _ in range(n))