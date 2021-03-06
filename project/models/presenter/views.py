from django.shortcuts import render

from project.models.presenter.helper import load_scripts


def presenter_view(request):
    scripts = load_scripts()
    return render(request, 'presenter.html', {'scripts': scripts})
