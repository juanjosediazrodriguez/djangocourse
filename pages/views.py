from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django import forms

def homePageView(request):
    return HttpResponse('Hello World!')

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context
    
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contacto - Tienda en línea",
            "subtitle": "Contáctanos",
            "email": "contacto@tiendaenlinea.com",
            "address": "Calle 50 #25-30, Medellín, Antioquia, Colombia",
            "phone": "+57 (4) 123-4567",
        })
        return context
    

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 1000},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 1800},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 1150},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 1150}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Productos - Tienda en línea"
        viewData["subtitle"] = "Lista de productos"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'
    
    def get(self, request, id):
        try:
            # Intentar obtener el producto
            product = Product.products[int(id)-1]
        except (IndexError, ValueError):
            # Si el ID es inválido, redirigir a home
            return HttpResponseRedirect(reverse('home'))
        
        viewData = {}
        viewData["title"] = product["name"] + " - Tienda en línea"
        viewData["subtitle"] = product["name"] + " - Información del producto"
        viewData["product"] = product
        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor a cero")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'
    
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Crear producto"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('success')  # ← Redirige a la página de éxito
        else:
            viewData = {}
            viewData["title"] = "Crear producto"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        

class ProductSuccessView(TemplateView):
    template_name = 'products/success.html'

