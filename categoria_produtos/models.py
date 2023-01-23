from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TbCategoriasProdutosFat(models.Model):

    categoria = models.TextField(max_length=70, null=False, blank=False)
    descricao = models.TextField(max_length=150, null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now=True)
    
