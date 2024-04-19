from django.db import models

class Texto(models.Model):
    conteudo_texto = models.TextField()