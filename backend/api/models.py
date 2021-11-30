from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    message = models.TextField(max_length=2000)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return self.title
