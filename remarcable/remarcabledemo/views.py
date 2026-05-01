from django.shortcuts import render
from django.db.models import Q
from remarcabledemo.models import Product, Tag, Category

# Create your views here.
"""
Views for the application, home is what the user initially 
sees when opening the app, product is what is displayed after a get request is made through the form.
"""


def home(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {"categories": categories, "tags": tags})


"""
The product view handles the queries to the database. 
After retrieving initial results based on search query parameter
the results are then filtered to only contain the selected tags and categories.
"""


def product(request):
    # get all tags and categories to display for search form
    tags = Tag.objects.all()
    categories = Category.objects.all()
    query = request.GET.get("query")
    products = Product.objects.all()
    tag_ids = request.GET.getlist("tag_filter")
    category_ids = request.GET.getlist("category_filter")
    if query:
        # case insensitive search for query on name and description
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    # filter products based on tag and category ids from query params
    if tag_ids:
        for tag_id in tag_ids:
            products = products.filter(tag__id=tag_id)
        products = products.distinct()
    if category_ids:
        for category_id in category_ids:
            products = products.filter(category__id=category_id)
        products = products.distinct()

    return render(
        request,
        "home.html",
        {"products": products, "categories": categories, "tags": tags},
    )
