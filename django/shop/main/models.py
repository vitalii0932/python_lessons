from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.
class Drugs(models.Model):
    name = models.CharField(max_length=40, default="Product name", unique=True)  # Unique name for the product
    short_description = models.CharField(max_length=100, default='Describe the product')  # Brief description
    image = models.ImageField(upload_to='static/assets/images/drugs/')
    price = models.DecimalField(max_digits=7, decimal_places=2)  # Price of the product
    price_with_discount = models.DecimalField(max_digits=7, decimal_places=2)  # Discounted price
    total_orders_count = models.PositiveIntegerField(default=0)  # Total number of orders for the product
    total_count_on_warehouse = models.PositiveIntegerField(default=0)  # Stock count in the warehouse
    sort_order = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)  # Visibility status of the product

    def __str__(self):
        return self.name  # String representation of the product

    def save(self, *args, **kwargs):
        """
        Override the save method to resize the image before saving the product.
        """

        """mini image"""
        # Target dimensions for the resized image
        mini_image_width = 300
        mini_image_height = 300

        # Open the uploaded mini image
        mini_image = Image.open(self.image)

        # Create a BytesIO object to hold the new image data
        output = self.resize_image(mini_image, mini_image_width, mini_image_height)
        # Move to the beginning of the output buffer

        # Replace the original image with the resized image
        self.image = InMemoryUploadedFile(
            output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
            'image/jpeg', sys.getsizeof(output), None
        )

        # Call the save method of the superclass to save the product
        super(Drugs, self).save(*args, **kwargs)

    def resize_image(self, old_image, width, height):
        output = BytesIO()
        # Create a new blank image with the target dimensions
        new_img = Image.new("RGB", (width, height), "white")

        # Calculate the aspect ratios
        aspect_ratio = old_image.width / old_image.height
        target_aspect_ratio = width / height

        # Resize and paste the image to maintain aspect ratio and fit within target dimensions
        if aspect_ratio > target_aspect_ratio:
            new_height = int(width / aspect_ratio)
            y_offset = (height - new_height) // 2
            old_image = old_image.resize((width, new_height))
            new_img.paste(old_image, (0, y_offset))
        else:
            new_width = int(height * aspect_ratio)
            x_offset = (width - new_width) // 2
            old_image = old_image.resize((new_width, height))
            new_img.paste(old_image, (x_offset, 0))

        # Save the resized image to the output buffer
        new_img.save(output, format='JPEG', quality=60)

        output.seek(0)

        return output

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'


class Cart(models.Model):
    session_id = models.CharField(max_length=255)  # This will hold the session ID
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} (Session: {self.session_id})"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cartitem_set.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.drug.price

    def __str__(self):
        return f"{self.quantity} of {self.drug.name}"