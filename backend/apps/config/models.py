from django.conf import settings
from django.db import models


class Image(models.Model):
    name = models.CharField("Nome", max_length=250, null=True, blank=True)
    image = models.ImageField("imagem", null=True, blank=True)

    created_at = models.DateTimeField("Criado em", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Criado em", auto_now=True, editable=False)

    def __str__(self) -> str:
        name = self.name or self.image or ""
        return f"{name}"


class Invite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário",
        null=False,
        blank=False,
    )
    engaged = models.CharField("Noivo", max_length=250, help_text="Nome do noivo")
    fiancee = models.CharField("Noiva", max_length=250, help_text="Nome da noiva")
    icon_center = models.ImageField("Imagem de centro")
    background_image = models.ImageField("Imagem de fundo")

    created_at = models.DateTimeField("Criado em", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Criado em", auto_now=True, editable=False)
