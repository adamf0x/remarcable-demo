import pytest
from remarcabledemo.models import Product, Tag, Category

# Create your tests here.
pytestmark = pytest.mark.django_db


# test products are properly created
def test_product_values():
    # add db entry
    tag = Tag.objects.create(tag_name="test tag")
    category = Category.objects.create(category_name="test category")
    product = Product.objects.create(
        name="test product", description="Test description", price=1.0
    )
    product.category.set([category])
    product.tag.set([tag])
    # ensure entry exists with correct attributes
    product = Product.objects.get(name="test product")
    tag = Tag.objects.get(tag_name="test tag")
    category = Category.objects.get(category_name="test category")
    assert product.name == "test product"
    assert product.description == "Test description"
    assert product.price == 1.0
    assert product.tag.first() == tag
    assert product.category.first() == category
