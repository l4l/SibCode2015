import string

import os
import random

from django.template import RequestContext, loader, Template

from CellManager.parser import XML
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from shutil import move, copyfile


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def show(request, id):
    t = loader.get_template('index.html')
    c = RequestContext(request, {'id': id + '.xml'})
    # xml = update_file('media/' + id)
    # xml.tree
    return HttpResponse(t.render(c),
        content_type="text/html")


def load(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        for key in request.FILES.keys():
            return HttpResponse(handle_uploaded_file(request.FILES[key]))

    else:
        form = UploadFileForm()
    return render_to_response('registration', {'form': form})


def handle_uploaded_file(file):
    file_name = new_name()

    destination = open(file_name + '.xml', 'wb+')

    for chunk in file.chunks():
        destination.write(chunk)

    destination.close()
    update_file(file_name + '.xml')
    move(file_name + '.xml', 'media/' + file_name + '.xml')
    return file_name


def update_file(file):
    xml = XML(file)
    xml.eval()
    xml.save(file)


def new(request):
    file_name = new_name()
    copyfile('static/template.xml', 'media/' + file_name + '.xml')
    return redirect('/' + file_name)


def new_name():
    file_name = random_string(10)
    while os.path.isfile(file_name + '.xml'):
        file_name = random_string(10)
    return file_name


def random_string(n):
    return ''.join(random
                   .SystemRandom()
                   .choice(string.ascii_uppercase + string.digits)
                   for _ in range(n))
