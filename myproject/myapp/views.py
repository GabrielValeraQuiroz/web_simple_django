from django.shortcuts import render

def home(request):
    context = {'nombre':'Gabriel Valera'}
    return render(request, 'home.html',context)