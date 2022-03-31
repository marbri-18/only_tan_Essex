from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.

def get_home(request):
    return render(request,'index.html')


class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.order_by('-created_on')
    template_name = 'products.html'
    paginate_by = 9

def get_events(request):
    return render(request,'events.html')

def get_about(request):
    return render(request,'about.html')

def get_contact(request):
    return render(request,'contact.html')
