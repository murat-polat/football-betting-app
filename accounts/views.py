from django.shortcuts import render

def Register(request, *args,**kwargs):
    return render(request, 'accounts/register.html')
