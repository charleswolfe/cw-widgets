from django.db import models


class Widget(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    number_of_parts = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.name, self.number_of_parts)
