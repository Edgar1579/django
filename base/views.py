from django.shortcuts import render

def inicio(request):
    titulo = "inicio"
    nombre = "Edgar Eduardo"
    context={
        "titulo": titulo,
        "nombre": nombre,
    }
    return render(request, 'index.html', context)

def contacto(request):
    titulo = "contacto"
    nombre = "Edgar Eduardo"
    context={
        "titulo": titulo,
    }
    return render(request, 'contacto.html', context)




