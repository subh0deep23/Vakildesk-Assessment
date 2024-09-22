from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    # Fetch the top 5 customers using the model method
    top_customers = Order.top_customers_in_last_six_months()
    
    # Pass the data to the template
    return render(request, 'orders/top_customers.html', {'top_customers': top_customers})
