from django.db import models

class StudentFee(models.Model):

    STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    )

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    fee_status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name