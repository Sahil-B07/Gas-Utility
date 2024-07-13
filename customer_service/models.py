from django.db import models
from django.contrib.auth.models import User


class CustomerAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class ServiceRequest(models.Model):
    REQUEST_TYPES = (
        ('Installation', 'Installation'),
        ('Maintenance', 'Maintenance'),
        ('Repair', 'Repair'),
    )
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(
        upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.request_type} - {self.customer.user.username}'
