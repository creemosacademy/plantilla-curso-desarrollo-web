from django.db import models
from django import forms

# Create your models here.


class Formulario(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()


class FomularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = (
            'name',
            'email',
            'message'
        )
