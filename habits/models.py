from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user} - {self.date}"