from django.db import models
from tickets.models import Purchase

class Transaction(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('completed', 'Completed')))
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.purchase.user.user.username} - {self.status}"

