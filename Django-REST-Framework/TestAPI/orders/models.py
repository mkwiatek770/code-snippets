from django.db import models


class Order(models.Model):
    # text fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    # date fields
    date_created = models.DateTimeField(auto_now_add=True)
    # bool
    is_active = models.BooleanField(default=True)
    # number fields
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # relations
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
