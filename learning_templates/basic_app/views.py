from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = { 'text': 'hello world', 'number': 100 }
    return render(request, 'basic_app/index.html', context_dict)

def others(request):
    return render(request, 'basic_app/others.html')

def relative(request):
    return render(request, 'basic_app/relative_templates.html')