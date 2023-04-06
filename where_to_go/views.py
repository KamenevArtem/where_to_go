from django.shortcuts import render


def show_greeting(request):
    return render(request, 'start_page.html')