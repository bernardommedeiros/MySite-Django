from django.db import models

# Create your models here.

class imcCalc(models.Model):
    peso = models.FloatField()
    altura = models.FloatField()
    imc = models.FloatField()
    condicao = models.CharField(max_length=50)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'IMC de {self.peso}kg e {self.altura}m = {self.imc:.2f}'
