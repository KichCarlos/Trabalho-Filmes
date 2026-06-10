from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.CharField(max_length=10)
    diretor = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    nota = models.FloatField()
    poster = models.URLField(blank=True)

    def __str__(self):
        return self.titulo