from django.db import models

class Edificio(models.Model):
    TIPO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    propietario = models.CharField("Nombre completo del propietario", max_length=150)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    num_cuartos = models.IntegerField("Número de cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name='departamentos')

    def __str__(self):
        return f"Depto en {self.edificio.nombre} - {self.propietario}"