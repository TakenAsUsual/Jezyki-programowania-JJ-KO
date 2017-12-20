from django.db import models


class Czynnosc(models.Model):
    nazwa = models.CharField(max_length=250)
    met = models.DecimalField(decimal_places=1, max_digits=5)

    def __str__(self):
        return self.nazwa
