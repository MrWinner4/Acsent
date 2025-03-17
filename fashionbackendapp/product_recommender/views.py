from django.shortcuts import render
from .models import Product, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
import numpy as np
import random
from sklearn.cluster import SpectralBiclustering
from .serializer import DataSerializer

@api_view (['GET']) #This is for getting data from the database
def getData(request):
     app = Product.objects.all()
     serializer = DataSerializer(app, many=True)
     return Response(serializer.data)

@api_view (['POST'])
def postData(request):
     serializer = DataSerializer(data = request.data)
     if(serializer.is_valid):
          serializer.save()
          return Response(serializer.data)

# Function to run recommendation
def recommend_product(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': 'You need to log in to get a recommendation.'})
    
    user_id = request.user.id  # This will get the authenticated user's ID

    num_products = 10  # Total number of products in the catalog
    products = [Product(f"Product {i+1}") for i in range(num_products)]
    num_users = 10  # Total number of users in the initial matrix
    users = [User(i, num_products) for i in range(num_users)]
    
def update_response(self, product_index, response):
        self.responses[product_index] = response

# View to handle product recommendation
def recommend_view(request):
    user_id = request.GET.get('user_id', None)
    if not user_id:
        return render(request, 'error.html', {'message': 'User ID is required.'})

    recommended_product = recommend_product(user_id)
    return render(request, 'recommendation.html', {'recommended_product': recommended_product})
