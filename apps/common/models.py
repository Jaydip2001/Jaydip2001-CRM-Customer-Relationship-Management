from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(
        max_length=50,
        choices=[("New", "New"), ("Contacted", "Contacted"), ("Converted", "Converted")],
        default="New"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Paid", "Paid"), ("Overdue", "Overdue")],
        default="Pending"
    )

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client.name}"
    

# Task Management


class Task(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    task_id = models.CharField(max_length=20, unique=True)
    task_name = models.CharField(max_length=40)
    date_issued = models.DateField(null=True)  # Make this field nullable
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Completed", "Completed"), ("Overdue", "Overdue")],
        default="Pending"
    )

    def __str__(self):
        return f"Task {self.task_number} - {self.client.name}"


# New Product model for your catalog
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

