from django.db import models

# Create your models here.
class Board(models.Model):
    board_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(maxlength=100, blank=True)
    contents = models.CharField(maxlength=500, blank=True)
    c_user = models.CharField(maxlength=10, blank=True)
    c_date = models.DateField(null=True, blank=True)
    hits = models.IntegerField(null=True, blank=True)
    