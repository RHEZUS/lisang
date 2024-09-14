from django.db import models
from events.models import Event
from django.conf import settings

class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.title}"

class Purchase(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.ticket_type.name}"

