from django import forms

class FileForm(forms.Form):
    file=forms.FileField(label="file")

class AddForm(forms.Form):
    nombre=forms.CharField(label="nombre")
    artista=forms.CharField(label="artista")
    genero=forms.CharField(label="genero")
    anio=forms.CharField(label="anio")
