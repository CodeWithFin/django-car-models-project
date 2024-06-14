from django.db import models

class carBrand(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
class carModel(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(carBrand,on_delete=models.CASCADE)
    year = models.IntegerField()
    horsepower = models.IntegerField()

    def __str__(self):
        return f"{self.brand.name} {self.name}"
    
