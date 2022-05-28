from django.db import models


class Image(models.Model):
    name = models.CharField("Nome", max_length=250, null=True, blank=True)
    image = models.ImageField("imagem", null=True, blank=True)

    created_at = models.DateTimeField("Criado em", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Criado em", auto_now=True, editable=False)

