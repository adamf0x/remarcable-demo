from django.shortcuts import render, HttpResponse
from django.db.models import Q, Count
from remarcabledemo.models import Product, Tag, Category

# Create your views here.
def home(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {"categories": categories, "tags": tags})

def product(request):
    # get all tags and categories to display for search form
    tags = Tag.objects.all()
    categories = Category.objects.all()
    # get query and all products initially 
    query = request.GET.get('query')
    products = Product.objects.all()
    # get tag and category id lists from get request
    tag_ids = request.GET.getlist('tag_filter')
    category_ids = request.GET.getlist('category_filter')
    # filter products based on search query if one was given
    if query:
        # case insensitive search for query on name and description 
        products = Product.objects.filter(Q(name__icontains = query) | Q(description__icontains = query))
    # filter queried products by selected tag ids if any were selected
    if tag_ids:
        # iterate through tag list filtering products that dont have the current tag id
        for tag_id in tag_ids:
            products = products.filter(tag__id=tag_id)
        products = products.distinct()
    # filter products previously queried and filtered by tag by selected category ids if any were selected
    if category_ids:
        for category_id in category_ids:
            products = products.filter(category__id=category_id)
        products = products.distinct()
    
    return render(request, "home.html", {"products" : products, "categories": categories, "tags": tags})