from django.shortcuts import render

def Perfil(request):
    return render(request, 'usuarios/perfil.html')
