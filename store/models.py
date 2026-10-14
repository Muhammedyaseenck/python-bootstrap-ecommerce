from django.db import models


class Product(models.Model):
    """A product sold in the store. Stored in a table named `Product`."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500)
    is_featured = models.BooleanField(
        default=False, help_text="Show this product in the home page carousel."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Product"
        ordering = ["-created_at", "-id"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Messages sent from the Contact Us page."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"