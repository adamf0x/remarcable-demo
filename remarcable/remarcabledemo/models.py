from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.tag_name
    
# Product model, has foreign keys for categories and tags
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ManyToManyField(Category, related_name="products")
    tag = models.ManyToManyField(Tag, related_name="products")

    def __str__(self):
        return self.name