from django.shortcuts import render, get_object_or_404
from .models import Classes

# Create your views here.


def classes(request):

    classes = Classes.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes.html', context)


def classes_detail(request, classes_id):

    classes = get_object_or_404(Classes, pk=classes_id)

    context = {
        'classes': classes,
    }

    return render(request, 'classes/classes_detail.html', context)
