# models.py
from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from PIL import Image

class News(models.Model):
    CATEGORY_CHOICES = [
        ('featured', 'Featured'),
        ('popular', 'Popular'),
        ('latest', 'Latest'),
        ('technology', 'Technology'),
        ('sports', 'Sports'),
        ('nieee', 'Nieee'),
        ('college', 'College')

    ]
    Filter_choices =[
        ('most_viewed', 'Most Viewed'),
        ('most_read', 'Most Read'),
        ('most_recent', 'Most Recent'),
    ]

    title = models.CharField(max_length=255)
    content = RichTextField(blank=True)
    image = CloudinaryField('image')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    filter = models.CharField(max_length=50, choices=Filter_choices, blank=True, null=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
