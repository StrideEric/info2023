from django.shortcuts import render

def Home(request):

	return render(request,'home.html')

def Contacto(request):

	return render(request,'contacto.html')

def Nosotros(request):

	return render(request,'nosotros.html')