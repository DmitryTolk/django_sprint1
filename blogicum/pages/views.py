# pages/views.py
from django.shortcuts import render
# Класс HttpResponse нужно импортировать в код из модуля django.http.
from django.http import HttpResponse

def about(request):    
    template_name = 'pages/about.html'
    return render(request, template_name)
    
def rules(request):    
    template_name = 'pages/rules.html'
    return render(request, template_name)