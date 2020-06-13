from django.db import models

# Create your models here.

CATEGORY_CHOICES =(
    ('D','Django'),
    ('R','React')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    custom_id= models.IntegerField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
