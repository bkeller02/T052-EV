from django.db import models


class ContactSupport(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    file_upload = models.FileField(
        null=True,
        blank=True,
        upload_to='contact/submissions/documents/',
        help_text='max. 42 megabytes',
    )

    class Meta:
        app_label  = 'main'

    def __str__(self):
        return self.subject

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # timestamp for when the form was submitted

    def __str__(self):
        return f"{self.full_name} - {self.subject}"