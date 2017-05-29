import os
from zipfile import ZipFile

from django.shortcuts import render, redirect
from django.http import HttpResponse
from lazarus import settings

from backend.models import TestSuite, TestSuiteForm


def unzip_report(report_id):
    path = "{0}/{1}".format(settings.MEDIA_ROOT, report_id)
    os.mkdir(path)
    report = TestSuite.objects.get(pk=report_id)
    _zip = ZipFile(report.result.path, mode="r")
    _zip.extractall(path)

def manage_upload(request):
    if request.method == 'GET':
        form = TestSuiteForm()
        return render(request, 'website/post_upload.html', {'form': form})
    elif request.method == 'POST':
        form = TestSuiteForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            unzip_report(obj.pk)
            # manage unzip of result
    return redirect('home')

def home(request):
    objs = TestSuite.objects.all()
    a = []
    for obj in objs:
        a.append("<li><a href='{url}'>{o.pk} - {o.created_at}</a></li>".format(
            o=obj, url='{0}/{1}'.format(settings.MEDIA_URL, obj.pk)))
    return HttpResponse("<html><ul>" + "".join(a) + "</ul></html>")
