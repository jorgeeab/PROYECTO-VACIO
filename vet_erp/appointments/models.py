from django.db import models
from clients.models import Pet

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, related_name='appointments', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pet.name} - {self.date_time}"
