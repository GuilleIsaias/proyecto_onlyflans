from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_id = models.AutoField(primary_key=True)
    flan_name = models.CharField(max_length=64)
    flan_description = models.TextField()
    flan_image_url = models.URLField()
    flan_slug = models.SlugField()
    flan_is_private = models.BooleanField()

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
