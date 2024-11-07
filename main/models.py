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
