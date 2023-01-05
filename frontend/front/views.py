from django.shortcuts import render
from .forms import FileForm,AddForm

import requests

servidor = 'http://127.0.0.1:5000/'

def home(request):
    contexto={
        'canciones':[]
    }
    try:
        response=requests.get(servidor+'canciones') #http://127.0.0.1:5000/canciones
        canciones=response.json()
        contexto['canciones']=canciones
    except:
        print('Error en la API')
    return render(request,'home.html',contexto)

def add(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=requests.post(servidor+'agregarCancion',json=json_data)
            if response.ok:
                return render(request,'add.html',{'form':form})
        return render(request,'add.html',{'form':form})
    return render(request,'add.html')

def cargaMasiva(request):
    ctx={
        'content':None,
        'response':None
    }
    if request.method=='POST':
        form=FileForm(request.POST, request.FILES)
        if form.is_valid():
            f=request.FILES['file']
            xml_binary=f.read()
            xml=xml_binary.decode('utf-8')
            ctx['content']=xml
            response=requests.post(servidor+'agregarCanciones',data=xml_binary)
            if response.ok:
                ctx['response']='ARCHIVO CARGADO CORRECTAMENTE'
            else:
                ctx['response']='ERROR, NO SE PUDO'
    else:
        return render(request,'carga.html')
    return render(request,'carga.html',ctx)

def ayuda(request):
    ctx={
        'title':'ayuda'
    }
    return render(request,'ayuda.html',ctx)

def eliminar(request):
    ctx={
        'title':'eliminar'
    }
    return render(request,'eliminar.html',ctx)