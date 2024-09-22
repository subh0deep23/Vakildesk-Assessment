from time import timezone
from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import User  # Assuming customer is a User

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Order {self.id} - {self.customer}'
    
    @classmethod
    def top_customers_in_last_six_months(cls):
        six_months_ago = timezone.now() - timezone.timedelta(days=6*30)
        return (cls.objects.filter(order_date__gte=six_months_ago, status='COMPLETED')
                .values('customer__username')
                .annotate(total_spent=models.Sum('total_amount'))
                .order_by('-total_spent')[:5])

