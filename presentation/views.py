from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from presentation.models import Presentation

# Create your views here.


def printable(request):
    p = get_object_or_404(Presentation, is_default=True)
    return render(request, 'print.html', locals())


def printable_slug(request, slug):
    p = get_object_or_404(Presentation, slug=slug)
    return render(request, 'print.html', locals())

def resume(request):
    p = get_object_or_404(Presentation, is_default=True)
    return render(request, 'resume.html', locals())

def resume_slug(request, slug):
    p = get_object_or_404(Presentation, slug=slug)
    return render(request, 'resume.html', locals())