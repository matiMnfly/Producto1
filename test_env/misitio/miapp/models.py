from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    Usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Nombre = models.CharField( max_length=200, null=None)
    Costo_presupuestado = models.BigIntegerField()
    Costo_real = models.BigIntegerField()
    Tienda = models.CharField(max_length=200)
    Notas = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Nombre
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()