from django.db import models

# Create your models here.


class Contact(models.Model):
    fname = models.CharField(max_length=200)
    sname = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"New message from {self.fname} {self.sname}: {self.body}"