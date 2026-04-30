from django.test import TestCase
from remarcabledemo.models import Product, Tag, Category

# Create your tests here.
class DemoTestCase(TestCase):
    def setUp(self):
        tag = Tag.objects.create(tag_name="test tag")
        category = Category.objects.create(category_name="test category")
        product = Product.objects.create(name="test product", description="Test description", price=1.0)
        product.category.set([category])
        product.tag.set([tag])
        
    # test products are properly created
    def test_product_values(self):
        product = Product.objects.get(name="test product")
        tag = Tag.objects.get(tag_name="test tag")
        category = Category.objects.get(category_name = "test category")
        self.assertEqual(product.name, "test product")
        self.assertEqual(product.description, "Test description")
        self.assertEqual(product.price, 1.0)
        self.assertEqual(product.tag.first(), tag)
        self.assertEqual(product.category.first(), category)