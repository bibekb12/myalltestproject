from django.db import models
from simple_history.models import HistoricalRecords

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField(default="False")
    history = HistoricalRecords() 

    def __str__(self):
        return self.question