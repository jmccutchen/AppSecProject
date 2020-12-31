from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def release(request):
    # return HttpResponse('<h1>This shit work?</h1>')
    return render(request, 'ReleaseManage/index.html')
