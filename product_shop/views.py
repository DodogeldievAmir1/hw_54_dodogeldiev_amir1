from django.shortcuts import render, redirect, get_object_or_404


def home_page(request):
    context = {
    }
    return render(request, 'index.html', context)
