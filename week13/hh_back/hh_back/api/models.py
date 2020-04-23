from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    city = models.CharField(max_length=300)
    address = models.TextField(default='')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address':  self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'Product id={self.id}, name={self.name}'

    def to_json(self):
        return{
            'id ': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,

        }

