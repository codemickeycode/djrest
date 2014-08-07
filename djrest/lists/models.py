from django.db import models

# Create your models here.
class ListItemGroup(models.Model):
    title = models.CharField(max_length=160)

class ListItem(models.Model):
    group = models.ForeignKey(ListItemGroup)
    item = models.TextField()

# 3 types of joins:
#OnetoOne - models.OneToOneField
#ManytoMany - models.ManyToManyField
#OnetoMany - models.ForeignKey